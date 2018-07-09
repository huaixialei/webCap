import core.util as util
import json

# print util.pcap_path
# print util.json_path

tdp = util.generate_tcpdump('sudo', "test")
print json.dumps(tdp.cmd)
