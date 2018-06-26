from tcpdump import Tcpdump
import os, shutil

pcap_path = os.path.abspath("tmp_pcap")
tcpdump_map = {}


def generate_tcpdump(cmd, key):
    tdp = Tcpdump(cmd)
    tcpdump_map[key] = tdp
    return tdp


def kill_tcpdump(key):
    if tcpdump_map.has_key(str):
        tcpdump_map[key].kill()
    return


def rm_pcap(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)


def rm_all_pcap():
    shutil.rmtree(pcap_path)
