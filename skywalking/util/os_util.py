# -*- coding:utf-8 -*-
# author：huawei
import os
import platform
import socket


def get_all_ipv4():
    ipv4 = set()
    addrs = socket.getaddrinfo(socket.gethostname(), None)
    for item in addrs:
        if ':' not in item[4][0] and "127.0.0.1" != item[4][0]:
            ipv4.add(item[4][0])
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ipv4.add(s.getsockname()[0])
    s.close()
    return ipv4


def get_host_name():
    return socket.gethostname()


def get_process_no():
    return os.getpid()


def get_os_name():
    return platform.system()


if __name__ == "__main__":
    print(get_all_ipv4())
    print(get_host_name())
    print(get_process_no())
    print(get_os_name())
