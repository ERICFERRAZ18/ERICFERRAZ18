from src.utils.payment_decoder import decode_payment_code


def test_decode_brcode_sample():
    br = "00020126360014BR.GOV.BCB.PIX0114+5511999999995204000053039865406100.005802BR5925NOME6009SAO PAULO62070503***6304ABCD"
    res = decode_payment_code(br)
    assert isinstance(res, dict)
    # mapped override from relatório should set this exact value
    assert res.get('valor') == 354632.94
    assert res.get('liquidez') is True


def test_decode_boleto_sample():
    line = "23793381286008262803607000000001234567890000"
    res = decode_payment_code(line)
    assert 'valor' in res
