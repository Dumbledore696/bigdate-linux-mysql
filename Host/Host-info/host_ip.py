# -*- coding: utf-8 -*-
#! python2
import psutil
#获取网卡名称和其ip地址，不包括回环
def get_netcard():
 netcard_info = []
 info = psutil.net_if_addrs()
 #Python (Dictionary) items() 函数以列表返回可遍历的(键, 值) 元组数组
 for k,v in info.items():
    for item in v:
        if item[0] == 2 and not item[1]=='127.0.0.1':#item[0]==2表示internet连接 即AF_INET是internet地址族，包括了tcp、udp什么的
            netcard_info.append(item[1])
 return netcard_info
# if __name__ == '__main__':
#  print get_netcard()