from tcpdump import Tcpdump

tcpdump_map = {}


def generate_tcpdump(cmd, key):
    tdp = Tcpdump(cmd)
    tcpdump_map[key] = tdp
    return tdp


def kill_tcpdump(key):
    if tcpdump_map.has_key(str):
        tcpdump_map[key].kill()
    return
