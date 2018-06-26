import dpkt


def t():
    t = open('t.pcap','rb')
    pcap = dpkt.pcap.Reader(t)

    lis = pcap.readpkts()
    print lis.__len__()
    # for ts, buf in pcap:
    #     eth = dpkt.ethernet.Ethernet(buf)
    #     ip = eth.data
    #     tcp = ip.data
    #     str = tcp.data
        # print str


t()