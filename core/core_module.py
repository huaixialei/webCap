# coding=utf-8
import subprocess, os


# Tcpdump wrapper factory
class TcpdumpFactory():
    tcpdump_map = {}

    def generate_tcpdump(self, cmd, key):
        tdp = Tcpdump(cmd)
        self.tcpdump_map[key] = tdp
        return tdp

    def kill_tcpdump(self, key):
        if self.tcpdump_map.has_key(str):
            self.tcpdump_map[key].kill()


# Tcpdump wrapper
class Tcpdump():
    popen = None
    cmd = ""

    def __init__(self, cmd):
        self.cmd = cmd

    def capture(self):
        redirect = " >> /dev/null"
        self.popen = subprocess.Popen(self.cmd + redirect, shell=True, stdout=None)
        return

    def kill(self):
        pid = self.popen.pid
        pgid = os.getpgid(pid)
        os.kill(pid, 15)
        os.killpg(pgid, 15)
        return


# Pcap file parser (parse with tcp/ip protocols)
class Parser():
    pass


# Tmp file path init, and tmp files cleaner
class Cleaner():
    __tmp_root_path__ = os.path.abspath("tmp")
    pcap_path = __tmp_root_path__ + "/pcap"
    json_path = __tmp_root_path__ + "/json"

    def init_path(self):
        if not os.path.exists(self.__tmp_root_path__):
            os.mkdir(self.__tmp_root_path__)
        if not os.path.exists(self.pcap_path):
            os.mkdir(self.pcap_path)
        if not os.path.exists(self.json_path):
            os.mkdir(self.json_path)

    def rm_pcap(self, pcap_name):
        tmp_path = self.pcap_path + "/" + pcap_name
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

    def rm_all_pcap(self):
        for i in os.listdir(self.pcap_path):
            self.rm_pcap(i)

    def rm_json(self, json_name):
        tmp_path = self.json_path + "/" + json_name
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

    def rm_all_json(self):
        for i in os.listdir(self.json_path):
            self.rm_json(i)
