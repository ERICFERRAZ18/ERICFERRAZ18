from datetime import datetime, timedelta
import re
import json
from pathlib import Path

BASE_BOLETO_DATE = datetime(1997, 10, 7).date()
_MAPPING_CACHE = None


def normalize(code: str) -> str:
    return re.sub(r'[^0-9A-Za-z]', '', code)


def load_mappings():
    global _MAPPING_CACHE
    if _MAPPING_CACHE is None:
        p = Path('.config/payment_mapping.json')
        if p.exists():
            try:
                _MAPPING_CACHE = json.loads(p.read_text(encoding='utf-8'))
            except Exception:
                _MAPPING_CACHE = {"mappings": [], "defaults": {"liquidez_threshold": 0.0}}
        else:
            _MAPPING_CACHE = {"mappings": [], "defaults": {"liquidez_threshold": 0.0}}
    return _MAPPING_CACHE


def apply_mappings(normalized_code: str):
    cfg = load_mappings()
    for rule in cfg.get('mappings', []):
        rtype = rule.get('type')
        pattern = rule.get('pattern') or ''
        if rtype == 'exact':
            if normalize(pattern) == normalized_code:
                valor = rule.get('valor_override')
                liquidez = rule.get('liquidez', valor is not None and valor > 0)
                return {
                    'valor': valor,
                    'vencimento': rule.get('vencimento'),
                    'liquidez': liquidez,
                    'reason': 'mapped_exact'
                }
        elif rtype == 'regex':
            try:
                if re.search(pattern, normalized_code):
                    valor = rule.get('valor_override')
                    liquidez = rule.get('liquidez', valor is not None and valor > 0)
                    return {
                        'valor': valor,
                        'vencimento': rule.get('vencimento'),
                        'liquidez': liquidez,
                        'reason': 'mapped_regex'
                    }
            except re.error:
                continue
    return None


def decode_brcode(brcode: str) -> dict:
    s = normalize(brcode)

    # attempt mappings first
    mapped = apply_mappings(s)
    if mapped:
        return {
            'valor': mapped.get('valor'),
            'vencimento': mapped.get('vencimento'),
            'liquidez': mapped.get('liquidez'),
            'codigo_normalizado': s,
            'reason': mapped.get('reason')
        }

    def find_tag(tag):
        idx = s.find(tag)
        if idx == -1:
            return None
        try:
            length = int(s[idx+2:idx+4])
            return s[idx+4: idx+4+length]
        except Exception:
            return None

    valor_str = find_tag('54')
    valor = None
    if valor_str:
        try:
            valor = float(valor_str.replace(',', '.'))
        except:
            valor = None
    liquidez = (valor is not None and valor > 0)
    return {"valor": round(valor, 2) if valor is not None else None, "vencimento": None, "liquidez": liquidez, "codigo_normalizado": s}


def decode_boleto(barcode: str) -> dict:
    s = re.sub(r'[^0-9]', '', barcode)
    # check mappings for boleto too
    mapped = apply_mappings(s)
    if mapped:
        return {
            'valor': mapped.get('valor'),
            'vencimento': mapped.get('vencimento'),
            'liquidez': mapped.get('liquidez'),
            'codigo_normalizado': s,
            'reason': mapped.get('reason')
        }

    if len(s) not in (44, 47, 48):
        raise ValueError("Código de boleto inválido (tamanho).")
    valor = None
    try:
        value_cents = int(s[-10:])
        valor = value_cents / 100.0
    except:
        valor = None

    vencimento = None
    try:
        if len(s) == 44:
            fator = int(s[5:9])
        else:
            fator = int(s[33:37])
        if fator > 0:
            vencimento = (BASE_BOLETO_DATE + timedelta(days=fator)).isoformat()
    except:
        vencimento = None

    liquidez = valor is not None and valor > 0
    return {"valor": round(valor,2) if valor is not None else None, "vencimento": vencimento, "liquidez": liquidez, "codigo_normalizado": s}


def decode_payment_code(code: str) -> dict:
    s = code.strip()
    normalized = normalize(s)

    # apply mappings first
    mapped = apply_mappings(normalized)
    if mapped:
        return {
            'valor': mapped.get('valor'),
            'vencimento': mapped.get('vencimento'),
            'liquidez': mapped.get('liquidez'),
            'codigo_normalizado': normalized,
            'reason': mapped.get('reason')
        }

    # heurística: BR Code (PIX) costuma iniciar com 000201
    if normalized.upper().startswith('000201') or 'BR' in normalized.upper():
        return decode_brcode(s)
    else:
        return decode_boleto(s)
