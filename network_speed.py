# -*- coding: utf-8 -*-
#! python2
import psutil
import os
import time
    #获取网卡名称不包括回环
def get_rxandtx():
    info = psutil.net_if_addrs()
    #Python (Dictionary) items() 函数以列表返回可遍历的(键, 值) 元组数组
    for k,v in info.items():
        for item in v:
            if item[0] == 2 and not item[1]=='127.0.0.1':#item[0]==2表示internet连接 即AF_INET是internet地址族，包括了tcp、udp什么的
                netcard=k
    start_time=time.time()
    #得到指定网卡的发送数据大小核接收数据大小
    f1= os.popen("cat /proc/net/dev | awk -F \| '$1~/"+netcard+"/' ").read().split()
    rx1=f1[1]
    tx1=f1[9]
    time.sleep(5)
    end_time=time.time()
    f2 = os.popen("cat /proc/net/dev | awk -F \| '$1~/" + netcard + "/' ").read().split()
    rx2=f2[1]
    tx2=f2[9]
    # print start_time
    rx1=float(rx1)
    tx1=float(tx1)
    # print end_time
    rx2=float(rx2)
    tx2=float(tx2)
    # print(rx1,rx2)
    # print(tx1,tx2)
    return( (rx2-rx1)/5/1000 , (tx2-tx1)/5/1000 )


