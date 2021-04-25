#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
from dubbo.client import DubboClient
import socket
import fcntl
import struct

SERVICE_LIST = {
        'common': (100000,'service_name'),

def get_ip(ifname): 
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
        inet = fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))
        ret = socket.inet_ntoa(inet[20:24]) 
        return ret 




if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage: %s service" % sys.argv[0]
        sys.exit()

    ip = get_ip('eth0')
    service = sys.argv[1]
    if not SERVICE_LIST.has_key(service):
        print 0
        sys.exit()
    port, interface = SERVICE_LIST.get(service)
    dubbo_cli = DubboClient( "%s" % interface , host='%s:%s' % (ip, port))
    try:
        res = dubbo_cli.call("check", "test", timeout=6)
        data = 0
        if res == "test OK":
            data = 1
    except:
        data = 0

    print data
    sys.exit()