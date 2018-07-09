# coding=utf-8
import subprocess, os


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
