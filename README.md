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
0     0 REDIRECT   tcp  --  *      *       0.0.0.0/0            127.0.0.1            tcp dpt:443 redir ports 8080
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
