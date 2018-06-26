from tcpdump import Tcpdump
import os, shutil

tmp_root_path = os.path.abspath("tmp")
pcap_path = tmp_root_path + "/pcap"
json_path = tmp_root_path + "/json"
tcpdump_map = {}

def init_path():
    if not os.path.exists(tmp_root_path):
        os.mkdir(tmp_root_path)
    if not os.path.exists(pcap_path):
        os.mkdir(pcap_path)
    if not os.path.exists(json_path):
        os.mkdir(json_path)


def generate_tcpdump(cmd, key):
    tdp = Tcpdump(cmd)
    tcpdump_map[key] = tdp
    return tdp


def kill_tcpdump(key):
    if tcpdump_map.has_key(str):
        tcpdump_map[key].kill()
    return


def rm_pcap(pcap_name):
    tmp_path = pcap_path + "/" + pcap_name
    if os.path.exists(tmp_path):
        os.remove(tmp_path)


def rm_all_pcap():
    for i in os.listdir(pcap_path):
        rm_pcap(i)