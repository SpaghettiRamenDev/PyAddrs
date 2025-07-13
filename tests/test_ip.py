from pyaddrs.ip6 import IP

def test_ip():
    addr = IP()
    assert str(addr[1][9][2][1][6][8][0][0][1][0][0][1]) == "192.168.001.001"
