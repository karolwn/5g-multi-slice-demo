import sys

from scapy.arch import get_if_addr
from scapy.layers.inet import ICMP, IP, Ether
from scapy.sendrecv import srp, srloop


def main(target: str, source_if: str) -> None:
    # ans, unans = sr(IP(dst=target) / ICMP(), timeout=3)
    # print(ans.summary(lambda s, r: r.sprintf("%IP.src% is alive")))
    print("pinging from interface {}".format(source_if))
    ping_req = IP(src=get_if_addr(source_if), dst=target)/ICMP()
    resp = srloop(ping_req, count=5)
    # resp = srp(ping_req, iface="uesimtun0")
    print(resp)


def ping_addr(host, count=6):
    packet = Ether(dst="ff:ff:ff:ff:ff:ff")/IP(dst=host)/ICMP()
    t=0.0
    for x in range(count):
        print(x)
        x += 1  # Start with x = 1 (not zero)
        ans, unans = srp(packet, iface="uesimtun0", filter='icmp', verbose=1)
        rx = ans[0][1]
        tx = ans[0][0]
        delta = rx.time - tx.sent_time
        print("ping #{0} rtt: {1} second".format(x, round(delta, 6)))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
    # ping_addr(sys.argv[1])
