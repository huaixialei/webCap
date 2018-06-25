# coding=utf-8
import subprocess, sys, os, signal

process_map = {}


class Tcpdump():
    popen = None

    def capture(self, cmd, process_key):
        redirect = " >> /dev/null"
        self.popen = subprocess.Popen(cmd + redirect, shell=True, stdout=None)
        process_map[process_key] = self

    def kill(self):
        os.kill(self.popen.pid, 9)
        os.killpg(os.getpgid(self.popen.pid), 9)
