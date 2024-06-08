- 👋 Hi, I’m @ERICFERRAZ18
- 👀 I’m interested in ...
- 🌱 I’m currently learning ...
- 💞️ I’m looking to collaborate on ...
- 📫 How to reach me ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...

<!---
ERICFERRAZ18/ERICFERRAZ18 is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
---> # cortar vias
iptables -F 
iptables -X 
iptables -Z 
iptables -v
Chain PREROUTING (policy ACCEPT 1 packets, 40 bytes)
pkts bytes target     prot opt in     out     source               destination         
0     0 REDIRECT   tcp  --  eth0   *       0.0.0.0/0            0.0.0.0/0            tcp dpt:80 redir ports 65535
0     0 REDIRECT   tcp  --  eth0   *       0.0.0.0/0            0.0.0.0/0            tcp dpt:443 redir ports 65535

Chain OUTPUT (policy ACCEPT 0000 packets, 65731 bytes)
pkts bytes target     prot opt in     out     source               destination         
0     0 REDIRECT   tcp  --  *      *       0.0.0.0/0            127.0.0.1            tcp dpt:80 redir ports 8080
0     0 REDIRECT   tcp  --  *      *       0.0.0.0/0            127.0.0.1            tcp dpt:443 redir ports 808
 Chain INPUT (policy ACCEPT 179M packets, 152G bytes)
 pkts bytes target     prot opt in     out     source               destination
 180M  153G UBIOS_INPUT_JUMP  all  --  *      *       0.0.0.0/0            0.0.0.0/0

Chain FORWARD (policy ACCEPT 1162M packets, 1380G bytes)
 pkts bytes target     prot opt in     out     source               destination
1163M 1381G UBIOS_FORWARD_JUMP  all  --  *      *       0.0.0.0/0            0.0.0.0/0

Chain OUTPUT (policy ACCEPT 181M packets, 152G bytes)
 pkts bytes target     prot opt in     out     source               destination
 181M  152G UBIOS_OUTPUT_JUMP  all  --  *      *       0.0.0.0/0            0.0.0.0/0

Chain UBIOS_FORWARD_IN_USER (1 references)
 pkts bytes target     prot opt in     out     source               destination
 457M  584G UBIOS_WAN_PF_IN_USER  all  --  eth4   *       0.0.0.0/0            0.0.0.0/0            /* 00000001095216663481 */
 457M  584G UBIOS_WAN_IN_USER  all  --  eth4   *       0.0.0.0/0            0.0.0.0/0            /* 00000001095216663482 */
 324M  308G UBIOS_LAN_IN_USER  all  --  br0    *       0.0.0.0/0            0.0.0.0/0            /* 00000001095216663483 */
 323M  471G UBIOS_LAN_IN_USER  all  --  br2    *       0.0.0.0/0            0.0.0.0/0            /* 00000001095216663484 */
5485K 1623M UBIOS_LAN_IN_USER  all  --  br3    *       0.0.0.0/0            0.0.0.0/0            /* 00000001095216663485 */
 752K  396M UBIOS_GUEST_IN_USER  all  --  br10   *       0.0.0.0/0            0.0.0.0/0            /* 00000001095216663486 */
  52M   15G UBIOS_GUEST_IN_USER  all  --  br20   *       0.0.0.0/0            0.0.0.0/0            /* 00000001095216663487 */

Chain UBIOS_FORWARD_JUMP (1 references)
 pkts bytes target     prot opt in     out     source               destination
 347M  414G UBIOS_FWD_IN_GEOIP_PRECHK  all  --  *      *       0.0.0.0/0            0.0.0.0/0
 347M  414G UBIOS_FWD_OUT_GEOIP_PRECHK  all  --  *      *       0.0.0.0/0            0.0.0.0/0
 347M  414G UBIOS_FORWARD_USER_HOOK  all  --  *      *       0.0.0.0/0            0.0.0.0/0

Chain UBIOS_FORWARD_OUT_USER (1 references)
 pkts bytes target     prot opt in     out     source               destination
 329M  288G UBIOS_WAN_PF_OUT_USER  all  --  *      eth4    0.0.0.0/0            0.0.0.0/0            /* 00000001095216663481 */
 329M  288G UBIOS_WAN_OUT_USER  all  --  *      eth4    0.0.0.0/0            0.0.0.0/0            /* 00000001095216663482 */
 692M  954G UBIOS_LAN_OUT_USER  all  --  *      br0     0.0.0.0/0            0.0.0.0/0            /* 00000001095216663483 */
  38M 2195M UBIOS_LAN_OUT_USER  all  --  *      br2     0.0.0.0/0            0.0.0.0/0            /* 00000001095216663484 */
  15M   33G UBIOS_LAN_OUT_USER  all  --  *      br3     0.0.0.0/0            0.0.0.0/0            /* 00000001095216663485 */
1340K 1667M UBIOS_GUEST_OUT_USER  all  --  *      br10    0.0.0.0/0            0.0.0.0/0            /* 00000001095216663486 */
  86M  101G UBIOS_GUEST_OUT_USER  all  --  *      br20    0.0.0.0/0            0.0.0.0/0            /* 00000001095216663487 */

Chain UBIOS_FORWARD_USER_HOOK (1 references)
 pkts bytes target     prot opt in     out     source               destination
1163M 1381G UBIOS_FORWARD_IN_USER  all  --  *      *       0.0.0.0/0            0.0.0.0/0            /* 00000001095216663481 */
1162M 1380G UBIOS_FORWARD_OUT_USER  all  --  *      *       0.0.0.0/0            0.0.0.0/0            /* 00000001095216663482 */

Chain UBIOS_FWD_IN_GEOIP_PRECHK (1 references)
 pkts bytes target     prot opt in     out     source               destination
 127M  120G UBIOS_IN_GEOIP  all  --  eth4   *       0.0.0.0/0            0.0.0.0/0

Chain UBIOS_FWD_OUT_GEOIP_PRECHK (1 references)
 pkts bytes target     prot opt in     out     source               destination
 114M  151G UBIOS_OUT_GEOIP  all  --  *      eth4    0.0.0.0/0            0.0.0.0/0

Chain UBIOS_GUEST_IN_USER (2 references)
 pkts bytes target     prot opt in     out     source               destination
 8632  605K RETURN     icmp --  *      *       0.0.0.0/0            0.0.0.0/0            icmptype 255 /* 00000001095216662480 */
    0     0 LOG        all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set UBIOS_6144fc439a3f340367486180 src match-set UBIOS_5f5f8979384ca905ec63b15c dst LOG flags 0 level 4
    0     0 DROP       all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set UBIOS_6144fc439a3f340367486180 src match-set UBIOS_5f5f8979384ca905ec63b15c dst /* 00000001095216662481 */
    0     0 RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set UBIOS_61606572a752e27e8cdff438 dst /* 00000001095216662482 */
    0     0 RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set UBIOS_5f5f8979384ca905ec63b15c src match-set UBIOS_5f6310ba1c017c0565ff114e dst /* 00000001095216662483 */
 1904  145K RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set UBIOS_5f5f8979384ca905ec63b15c src match-set UBIOS_5f5f8a0a384ca905ec63b15e dst /* 00000001095216662484 */
 6485  381K RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set UBIOS_5f5f8979384ca905ec63b15c src match-set UBIOS_5f630f3c1c017c0565ff111e dst match-set UBIOS_5f630f6e1c017c0565ff1130 dst /* 00000001095216662485 */
  475 76823 RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set UBIOS_5f67a7c31c017c0565010767 src match-set UBIOS_5f67a98c1c017c0565012d04 dst match-set UBIOS_5f6805a21c017c056506fca6 dst /* 00000001095216662486 */
 962K   75M RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set UBIOS_5f630fe91c017c0565ff1133 src match-set UBIOS_5f67a98c1c017c0565012d04 dst match-set UBIOS_5f6805a21c017c056506fca6 dst /* 00000001095216662487 */
5035K  344M RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set UBIOS_5f680b251c017c056506fd35 src match-set UBIOS_5f67a98c1c017c0565012d04 dst match-set UBIOS_5f6805a21c017c056506fca6 dst /* 00000001095216662488 */
    0     0 RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set UBIOS_5f67a98c1c017c0565012d04 src match-set UBIOS_5f5f8979384ca905ec63b15c dst /* 00000001095216662489 */
  44M   14G RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set UBIOS_5f5f8979384ca905ec63b15c src match-set UBIOS_5f5f9563384ca905ec63b250 dst ctstate RELATED,ESTABLISHED /* 00000001095216662490 */
   39  2028 RETURN     tcp  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set UBIOS_5f5f8979384ca905ec63b15c src match-set UBIOS_5f67aab41c017c05650184d7 dst match-set UBIOS_61525282a752e27e8cde94d6 dst /* 00000000004294969307 */
 223K   13M LOG        all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set UBIOS_5f5f8979384ca905ec63b15c src match-set UBIOS_5f5f8979384ca905ec63b15c dst LOG flags 0 level 4
 711K   41M DROP       all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set UBIOS_5f5f8979384ca905ec63b15c src match-set UBIOS_5f5f8979384ca905ec63b15c dst /* 00000001095216662492 */
  123  6396 RETURN     tcp  --  *      *       0.0.0.0/0            0.0.0.0/0            tcp dpt:53 /* 00000000004294970297 */
 5671  423K RETURN     udp  --  *      *       0.0.0.0/0            0.0.0.0/0            udp dpt:53 /* 00000000008589937593 */
    0     0 RETURN     tcp  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set UBIOS_captive_portal_subnets dst tcp dpt:443 /* 00000000004294970298 */
    0     0 RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set UBIOS_guest_pre_allow dst /* 00000001095216663483 */
 7793  616K DROP       all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set UBIOS_guest_restricted dst /* 00000001095216663484 */
    0     0 DROP       all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set UBIOS_corporate_network dst /* 00000001095216663485 */
    0     0 DROP       all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set UBIOS_remote_user_vpn_network dst /* 00000001095216663486 */
 745K  395M RETURN     all  --  *      *       192.168.10.0/24      0.0.0.0/0            /* 00000001095216666481 */
1167K  486M RETURN     all  --  *      *       192.168.20.0/24      0.0.0.0/0            /* 00000001095216666482 */
   50  6248 RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0            /* 00000001097364144127 */

Chain UBIOS_GUEST_LOCAL_USER (2 references)
 pkts bytes target     prot opt in     out     source               destination
2419K  194M RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0            /* 00000001095216662480 */
    0     0 RETURN     tcp  --  *      *       0.0.0.0/0            0.0.0.0/0            tcp dpt:53 /* 00000000004294970297 */
    0     0 RETURN     udp  --  *      *       0.0.0.0/0            0.0.0.0/0            udp dpt:53 /* 00000000008589937593 */
    0     0 RETURN     icmp --  *      *       0.0.0.0/0            0.0.0.0/0            /* 00000001095216663482 */
    0     0 RETURN     udp  --  *      *       0.0.0.0/0            0.0.0.0/0            udp spt:68 dpt:67 /* 00000000008589937595 */
    0     0 DROP       all  --  *      *       0.0.0.0/0            0.0.0.0/0            /* 00000001097364144127 */

Chain UBIOS_GUEST_OUT_USER (2 references)
 pkts bytes target     prot opt in     out     source               destination
  87M  103G RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0            ctstate RELATED,ESTABLISHED /* 00000001095216662480 */
 3665  319K LOG        all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set UBIOS_5f5f8979384ca905ec63b15c src match-set UBIOS_5f5f8979384ca905ec63b15c dst LOG flags 0 level 4
 6621  604K DROP       all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set UBIOS_5f5f8979384ca905ec63b15c src match-set UBIOS_5f5f8979384ca905ec63b15c dst /* 00000001095216662481 */
   20  1040 RETURN     all  --  *      *       0.0.0.0/0            192.168.10.0/24      /* 00000001095216666481 */
    0     0 RETURN     all  --  *      *       0.0.0.0/0            192.168.20.0/24      /* 00000001095216666482 */
    0     0 RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0            /* 00000001097364144127 */

Chain UBIOS_INPUT_GEOIP_PRECHK (1 references)
 pkts bytes target     prot opt in     out     source               destination
1948K  182M UBIOS_IN_GEOIP  all  --  eth4   *       0.0.0.0/0            0.0.0.0/0

Chain UBIOS_INPUT_JUMP (1 references)
 pkts bytes target     prot opt in     out     source               destination
  55M   46G UBIOS_INPUT_GEOIP_PRECHK  all  --  *      *       0.0.0.0/0            0.0.0.0/0
  55M   46G UBIOS_INPUT_USER_HOOK  all  --  *      *       0.0.0.0/0            0.0.0.0/0

Chain UBIOS_INPUT_USER_HOOK (1 references)
 pkts bytes target     prot opt in     out     source               destination
6220K  713M UBIOS_WAN_LOCAL_USER  all  --  eth4   *       0.0.0.0/0            0.0.0.0/0            /* 00000001095216663481 */
 964K   81M UBIOS_LAN_LOCAL_USER  all  --  br0    *       0.0.0.0/0            0.0.0.0/0            /* 00000001095216663482 */
2025K 1091M UBIOS_LAN_LOCAL_USER  all  --  br2    *       0.0.0.0/0            0.0.0.0/0            /* 00000001095216663483 */
 894K   72M UBIOS_LAN_LOCAL_USER  all  --  br3    *       0.0.0.0/0            0.0.0.0/0            /* 00000001095216663484 */
 870K   70M UBIOS_GUEST_LOCAL_USER  all  --  br10   *       0.0.0.0/0            0.0.0.0/0            /* 00000001095216663485 */
1549K  124M UBIOS_GUEST_LOCAL_USER  all  --  br20   *       0.0.0.0/0            0.0.0.0/0            /* 00000001095216663486 */

Chain UBIOS_IN_GEOIP (2 references)
 pkts bytes target     prot opt in     out     source               destination
    0     0 RETURN     all  --  *      *       0.0.0.0              0.0.0.0/0
    0     0 RETURN     all  --  *      *       255.255.255.255      0.0.0.0/0
    0     0 RETURN     all  --  *      *       127.0.0.0/8          0.0.0.0/0
    0     0 RETURN     all  --  *      *       192.168.10.0/24      0.0.0.0/0
    0     0 RETURN     all  --  *      *       192.168.2.0/24       0.0.0.0/0
    0     0 RETURN     all  --  *      *       192.168.20.0/24      0.0.0.0/0
    0     0 RETURN     all  --  *      *       192.168.3.0/24       0.0.0.0/0
    0     0 RETURN     all  --  *      *       25.0.0.0/24          0.0.0.0/0
    0     0 RETURN     all  --  *      *       97.81.124.0/22       0.0.0.0/0
    0     0 RETURN     all  --  *      *       10.0.0.0/8           0.0.0.0/0
    0     0 RETURN     all  --  *      *       172.16.0.0/12        0.0.0.0/0
    0     0 RETURN     all  --  *      *       192.168.0.0/16       0.0.0.0/0
    0     0 RETURN     all  --  *      *       100.64.0.0/10        0.0.0.0/0
    0     0 RETURN     all  --  *      *       169.254.0.0/16       0.0.0.0/0
 128M  120G RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0            state RELATED,ESTABLISHED
25210 2359K DROP       all  --  *      *       0.0.0.0/0            0.0.0.0/0            -m geoip --source-country CN
 509K   54M RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0

Chain UBIOS_LAN_IN_USER (3 references)
 pkts bytes target     prot opt in     out     source               destination
85277 6707K RETURN     icmp --  *      *       0.0.0.0/0            0.0.0.0/0            icmptype 255 /* 00000001095216662480 */
    0     0 RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set UBIOS_5f5f8979384ca905ec63b15c src match-set UBIOS_5f6310ba1c017c0565ff114e dst /* 00000001095216662481 */
 3725  285K RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set UBIOS_5f5f8979384ca905ec63b15c src match-set UBIOS_5f5f8a0a384ca905ec63b15e dst /* 00000001095216662482 */
    0     0 RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set UBIOS_5f5f8979384ca905ec63b15c src match-set UBIOS_5f630f3c1c017c0565ff111e dst match-set UBIOS_5f630f6e1c017c0565ff1130 dst /* 00000001095216662483 */
    0     0 RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set UBIOS_5f67a7c31c017c0565010767 src match-set UBIOS_5f67a98c1c017c0565012d04 dst match-set UBIOS_5f6805a21c017c056506fca6 dst /* 00000001095216662484 */
    0     0 RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set UBIOS_5f630fe91c017c0565ff1133 src match-set UBIOS_5f67a98c1c017c0565012d04 dst match-set UBIOS_5f6805a21c017c056506fca6 dst /* 00000001095216662485 */
 8726 9206K RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set UBIOS_5f5f8979384ca905ec63b15c src match-set UBIOS_5f67aab41c017c05650184d7 dst /* 00000001095216662486 */
1927K  153M RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set UBIOS_5f680b251c017c056506fd35 src match-set UBIOS_5f67a98c1c017c0565012d04 dst match-set UBIOS_5f6805a21c017c056506fca6 dst /* 00000001095216662487 */
 156K   10M RETURN     udp  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set UBIOS_5f5f8979384ca905ec63b15c src match-set UBIOS_5f68142d1c017c056506fe88 dst /* 00000000008589936600 */
  35M 1843M RETURN     tcp  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set UBIOS_5f67a98c1c017c0565012d04 src match-set UBIOS_5f67a96c1c017c05650123b8 dst match-set UBIOS_61420febf9b1a9036b0fda76 dst /* 00000000004294969305 */
    0     0 RETURN     tcp  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set UBIOS_5f67a98c1c017c0565012d04 src match-set UBIOS_5f67a98c1c017c0565012d04 dst match-set UBIOS_614230d6f9b1a9036b0fdde4 dst /* 00000000004294969306 */
  12M   35G RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set UBIOS_5f67a98c1c017c0565012d04 src match-set UBIOS_5f5f8979384ca905ec63b15c dst /* 00000001095216662491 */
 602M  744G RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set UBIOS_5f5f8979384ca905ec63b15c src match-set UBIOS_5f5f9563384ca905ec63b250 dst ctstate RELATED,ESTABLISHED /* 00000001095216662492 */
  172  8944 LOG        all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set UBIOS_5f5f8979384ca905ec63b15c src match-set UBIOS_5f5f8979384ca905ec63b15c dst LOG flags 0 level 4
  657 34164 DROP       all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set UBIOS_5f5f8979384ca905ec63b15c src match-set UBIOS_5f5f8979384ca905ec63b15c dst /* 00000001095216662493 */
 766K   78M RETURN     all  --  *      *       25.0.0.0/24          0.0.0.0/0            /* 00000001095216666481 */
 457K  101M RETURN     all  --  *      *       192.168.2.0/24       0.0.0.0/0            /* 00000001095216666482 */
26039 4472K RETURN     all  --  *      *       192.168.3.0/24       0.0.0.0/0            /* 00000001095216666483 */
    0     0 RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0            /* 00000001097364144127 */

Chain UBIOS_LAN_LOCAL_USER (3 references)
 pkts bytes target     prot opt in     out     source               destination
3882K 1244M RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0            /* 00000001097364144127 */

Chain UBIOS_LAN_OUT_USER (3 references)
 pkts bytes target     prot opt in     out     source               destination
 745M  989G RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0            ctstate RELATED,ESTABLISHED /* 00000001095216662480 */
    0     0 RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set UBIOS_5f6310ba1c017c0565ff114e src match-set UBIOS_5f5f8979384ca905ec63b15c dst /* 00000001095216662481 */
 181K   11M RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0            /* 00000001095216662482 */
    0     0 RETURN     all  --  *      *       0.0.0.0/0            25.0.0.0/24          /* 00000001095216666481 */
    0     0 RETURN     all  --  *      *       0.0.0.0/0            192.168.2.0/24       /* 00000001095216666482 */
    0     0 RETURN     all  --  *      *       0.0.0.0/0            192.168.3.0/24       /* 00000001095216666483 */
    0     0 RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0            /* 00000001097364144127 */

Chain UBIOS_OUTPUT_JUMP (1 references)
 pkts bytes target     prot opt in     out     source               destination

Chain UBIOS_OUTPUT_USER_HOOK (0 references)
 pkts bytes target     prot opt in     out     source               destination

Chain UBIOS_OUT_GEOIP (1 references)
 pkts bytes target     prot opt in     out     source               destination
    0     0 RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0
    0     0 RETURN     all  --  *      *       0.0.0.0/0            255.255.255.255
    0     0 RETURN     all  --  *      *       0.0.0.0/0            127.0.0.0/8
    0     0 RETURN     all  --  *      *       0.0.0.0/0            192.168.10.0/24
    0     0 RETURN     all  --  *      *       0.0.0.0/0            192.168.2.0/24
    0     0 RETURN     all  --  *      *       0.0.0.0/0            192.168.20.0/24
    0     0 RETURN     all  --  *      *       0.0.0.0/0            192.168.3.0/24
    0     0 RETURN     all  --  *      *       0.0.0.0/0            25.0.0.0/24
    0     0 RETURN     all  --  *      *       0.0.0.0/0            97.81.124.0/22
  271 27973 RETURN     all  --  *      *       0.0.0.0/0            10.0.0.0/8
  404 24832 RETURN     all  --  *      *       0.0.0.0/0            172.16.0.0/12
  657 44721 RETURN     all  --  *      *       0.0.0.0/0            192.168.0.0/16
   12  1586 RETURN     all  --  *      *       0.0.0.0/0            100.64.0.0/10
    0     0 RETURN     all  --  *      *       0.0.0.0/0            169.254.0.0/16
 114M  151G RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0            state RELATED,ESTABLISHED
 4754  640K DROP       all  --  *      *       0.0.0.0/0            0.0.0.0/0            -m geoip --destination-country CN
 756K  202M RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0

Chain UBIOS_WAN_IN_USER (1 references)
 pkts bytes target     prot opt in     out     source               destination
 457M  584G RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0            ctstate RELATED,ESTABLISHED /* 00000001095216663481 */
    0     0 DROP       all  --  *      *       0.0.0.0/0            0.0.0.0/0            ctstate INVALID /* 00000001095216663482 */
  379 15952 RETURN     tcp  --  *      *       0.0.0.0/0            25.0.0.151           multiport dports 30000:30031 /* 00000000004294970301 */
 7999  928K RETURN     udp  --  *      *       0.0.0.0/0            25.0.0.151           multiport dports 30000:30031 /* 00000000008589937597 */
63858 4053K RETURN     tcp  --  *      *       0.0.0.0/0            25.0.0.151           tcp dpt:32400 /* 00000000004294970302 */
 4133  248K RETURN     tcp  --  *      *       0.0.0.0/0            25.0.0.151           tcp dpt:5000 /* 00000000004294970303 */
 2077  119K RETURN     tcp  --  *      *       0.0.0.0/0            25.0.0.151           tcp dpt:143 /* 00000000004294970304 */
84007 4344K RETURN     tcp  --  *      *       0.0.0.0/0            25.0.0.151           tcp dpt:8000 /* 00000000004294970305 */
   16   647 RETURN     udp  --  *      *       0.0.0.0/0            25.0.0.151           udp dpt:8000 /* 00000000008589937601 */
  346 14564 RETURN     tcp  --  *      *       0.0.0.0/0            25.0.0.151           tcp dpt:21 /* 00000000004294970306 */
    0     0 RETURN     udp  --  *      *       0.0.0.0/0            25.0.0.151           udp dpt:21 /* 00000000008589937602 */
 1251 51548 RETURN     tcp  --  *      *       0.0.0.0/0            25.0.0.151           tcp dpt:3389 /* 00000000004294970307 */
   69  9130 RETURN     udp  --  *      *       0.0.0.0/0            25.0.0.151           udp dpt:3389 /* 00000000008589937603 */
    0     0 DROP       all  --  *      *       0.0.0.0/0            0.0.0.0/0            /* 00000001097364144127 */

Chain UBIOS_WAN_LOCAL_USER (1 references)
 pkts bytes target     prot opt in     out     source               destination
4941K  574M RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0            ctstate RELATED,ESTABLISHED /* 00000001095216663481 */
48282 2139K DROP       all  --  *      *       0.0.0.0/0            0.0.0.0/0            ctstate INVALID /* 00000001095216663482 */
1231K  136M DROP       all  --  *      *       0.0.0.0/0            0.0.0.0/0            /* 00000001097364144127 */

Chain UBIOS_WAN_OUT_USER (1 references)
 pkts bytes target     prot opt in     out     source               destination
  849 44148 DROP       all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set UBIOS_5f5fb64f384ca905ec63b4ea dst /* 00000001095216662480 */
    0     0 DROP       all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set UBIOS_5f5f8979384ca905ec63b15c dst /* 00000001095216662481 */
  247 13404 REJECT     all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set UBIOS_5f8bcc47d508430616390bfe dst /* 00000001095216662482 */ reject-with icmp-port-unreachable
 329M  288G RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0            /* 00000001097364144127 */

Chain UBIOS_WAN_PF_IN_USER (1 references)
 pkts bytes target     prot opt in     out     source               destination
 205K   19M RETURN     tcp  --  *      *       0.0.0.0/0            25.0.0.151           tcp dpt:143 /* 00000000004505618797 */
 1251 51548 RETURN     tcp  --  *      *       0.0.0.0/0            25.0.0.151           tcp dpt:3389 /* 00000000005345189507 */
   69  9130 RETURN     udp  --  *      *       0.0.0.0/0            25.0.0.151           udp dpt:3389 /* 00000000009640156803 */
48148 5655K RETURN     tcp  --  *      *       0.0.0.0/0            25.0.0.151           tcp dpt:5000 /* 00000000005651687971 */
84007 4344K RETURN     tcp  --  *      *       0.0.0.0/0            25.0.0.151           tcp dpt:8000 /* 00000000005736769785 */
   16   647 RETURN     udp  --  *      *       0.0.0.0/0            25.0.0.151           udp dpt:8000 /* 00000000010031737081 */
  36M 2386M RETURN     tcp  --  *      *       0.0.0.0/0            25.0.0.151           tcp dpt:32400 /* 00000000005747484663 */
  379 15952 RETURN     tcp  --  *      *       0.0.0.0/0            25.0.0.151           multiport dports 30000:30031 /* 00000000006180480729 */
 7999  928K RETURN     udp  --  *      *       0.0.0.0/0            25.0.0.151           multiport dports 30000:30031 /* 00000000010475448025 */
  346 14564 RETURN     tcp  --  *      *       0.0.0.0/0            25.0.0.151           tcp dpt:21 /* 00000000006342261859 */
    0     0 RETURN     udp  --  *      *       0.0.0.0/0            25.0.0.151           udp dpt:21 /* 00000000010637229155 */

Chain UBIOS_WAN_PF_OUT_USER (1 references)
 pkts bytes target     prot opt in     out     source               destination
 427K  175M RETURN     tcp  --  *      *       25.0.0.151           0.0.0.0/0            tcp spt:143 /* 00000000004505618797 */
 1251 50040 RETURN     tcp  --  *      *       25.0.0.151           0.0.0.0/0            tcp spt:3389 /* 00000000005345189507 */
    0     0 RETURN     udp  --  *      *       25.0.0.151           0.0.0.0/0            udp spt:3389 /* 00000000009640156803 */
66883   79M RETURN     tcp  --  *      *       25.0.0.151           0.0.0.0/0            tcp spt:5000 /* 00000000005651687971 */
83979 3359K RETURN     tcp  --  *      *       25.0.0.151           0.0.0.0/0            tcp spt:8000 /* 00000000005736769785 */
    0     0 RETURN     udp  --  *      *       25.0.0.151           0.0.0.0/0            udp spt:8000 /* 00000000010031737081 */
 102M  166G RETURN     tcp  --  *      *       25.0.0.151           0.0.0.0/0            tcp spt:32400 /* 00000000005747484663 */
  378 15120 RETURN     tcp  --  *      *       25.0.0.151           0.0.0.0/0            multiport sports 30000:30031 /* 00000000006180480729 */
    0     0 RETURN     udp  --  *      *       25.0.0.151           0.0.0.0/0            multiport sports 30000:30031 /* 00000000010475448025 */
  346 13840 RETURN     tcp  --  *      *       25.0.0.151           0.0.0.0/0            tcp spt:21 /* 00000000006342261859 */
    0     0 RETURN     udp  --  *      *       25.0.0.151           0.0.0.0/0            udp spt:21 /* 00000000010637229155 */

[root@localhost ~]# consoletype
pty
pfctl -e
pfctl -f /etc/pf.conf # Load the pf.conf file
pfctl -nf /etc/pf.conf # parse the file, but do not load
pfctl -Nf /etc/pf.conf # Only load the NAT rules in the file
pfctl -Rf /etc/pf.conf # Only load the filter rules in the file
pfctl -sn # Display the current NAT rules
pfctl -sr # Display the current filtering rules
pfctl -ss # Display the current status table
pfctl -si # Display filtering status and count
pfctl -sa # display any displayable
iptables -A INPUT -s 192.168.1.0/24 -p tcp --dport 22 -j ACCEPT
iptables -I INPUT -j DROP -p tcp -s 0.0.0.0/0 -m string --algo kmp --string
iptables -A INPUT -p tcp --syn -m limit --limit 5/second -j ACCEPT

