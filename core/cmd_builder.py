class Builder:
    def build(inte,src_ip,dst_ip,dst_port,src_mac,dst_mac):
        cmd = ' tcpdump -i ' + inte
        cmd = cmd + " ' "
        cmd = cmd + " ( " + tcp + " )&& "
        cmd = cmd + " ( src host " + src_ip + " )&& "
        cmd = cmd + " ( dst host " + dst_ip + " )&& "
        cmd = cmd + " ( dst port " + dst_port + " )&& "
        
        cmd = cmd + " ' "


    def buildInte(cmd,inte):
        cmd = cmd + "tcpdump -i " + inte
        return cmd


    def buildWrite(cmd,root_path,file_name):
        cmd = cmd + " -w " + root_path + "/" + file_name
        return cmd


    def buildFilter(cmd,src_ip,dst_ip,dst_port,src_mac,dst_mac):
        src_ip = 
