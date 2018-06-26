from tcpdump import Tcpdump
import sys

tcpdump_map = {}


def generate_tcpdump(cmd, key):
    tdp = Tcpdump(cmd)
    tcpdump_map[key] = tdp
    return tdp


def kill_tcpdump(key):
    if tcpdump_map.has_key(str):
        tcpdump_map[key].kill()
    return


# &&(tcp[(tcp[12:1]>>2):2] == 0x4745)
t = generate_tcpdump("tcpdump -i en4 -w t.pcap '(tcp)&&(src host 10.10.32.35)'", 'shut\n')
t.capture()

while True:
    str = sys.stdin.readline()
    if tcpdump_map.has_key(str):
        kill_tcpdump(str)
        break

# t()
