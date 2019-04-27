# encoding: utf-8
from __future__ import division
import sys
#sys.path.append('/./home/njit/PycharmProjects/Host/venv/lib/python2.7/site-packages')
sys.path.append('/./home/hadoop/桌面/Host/venv/lib/python2.7/site-packages')

import  os
import pymysql
import time, conf
import socket
import disk_used, mem_used, cpu_used, Average_load, host_ip,get_cpuinfo , judge_exist , network_speed


# 连接数据库，定义游标
conn = pymysql.connect(user=conf.user, passwd=conf.passwd, host=conf.host, port=conf.port)
cur = conn.cursor()


# 创建数据库和表
try:
    if judge_exist.database_exist(cur,'collection')!=1 :
        cur.execute("create database collection")
    else:
        print ("use old database")
except Exception, e:
    print ("Error:creat database ")
conn.select_db("collection")
try:
    if judge_exist.table_exist(cur,'cpu_dynamic_info')!=1:
        cur.execute("CREATE TABLE `cpu_dynamic_info` (`ID`  int PRIMARY KEY AUTO_INCREMENT ,`hostID`  int NULL ,`usage`  varchar(50) NULL ,`mytime`  varchar(50) NULL )")
    else:
        print ("use old table")
except Exception, e1:
    print ("Error:creat table cpu_dynamic_info ")
try:
    if judge_exist.table_exist(cur,'mem_dynamic_info')!=1:
        cur.execute("CREATE TABLE `mem_dynamic_info` (`ID`  int PRIMARY KEY AUTO_INCREMENT ,`hostID`  int NULL ,`usage`  varchar(50) NULL ,`mytime`  varchar(50) NULL )")
    else:
        print ("use old table")
except Exception, e2:
    print ("Error:creat table mem_dynamic_info ")
try:
    if judge_exist.table_exist(cur,'disk_dynamic_info')!=1:
        cur.execute("CREATE TABLE `disk_dynamic_info` (`ID`  int PRIMARY KEY AUTO_INCREMENT ,`hostID`  int NULL ,`usage`  varchar(50) NULL ,`mytime`  varchar(50) NULL )")
    else:
        print ("use old table")
except Exception, e3:
    print ("Error:creat table disk_dynamic_info ")
try:
    if judge_exist.table_exist(cur,'network_dynamic_info')!=1:
        cur.execute("CREATE TABLE `network_dynamic_info` (`ID`  int PRIMARY KEY AUTO_INCREMENT ,`hostID`  int NULL ,`receive_speed`  varchar(50) NULL , `transmit_speed`  varchar(50) NULL,`mytime`  varchar(50) NULL )")
    else:
        print ("use old table")
except Exception, e3:
    print ("Error:creat table disk_dynamic_info ")
try:
    if judge_exist.table_exist(cur,'server_info')!=1:
        cur.execute("CREATE TABLE `server_info` (`ID`  int PRIMARY KEY AUTO_INCREMENT ,`节点名称`  varchar(255) NULL ,`IP地址`  varchar(255) NULL ,`服务器类型`  varchar(255) NULL ,`cpu型号`  varchar(255) NULL ,`cpu核数`  varchar(255) NULL ,`内存`  varchar(255) NULL ,`磁盘空间`  varchar(255) NULL ,`录入时间`  varchar(255) NULL ,`修改时间`  varchar(255) NULL ,`是否安装agent`  enum('1','0') CHARACTER SET utf8 NULL DEFAULT '0' COMMENT '0为未安装' ,`备注`  varchar(255) NULL  )")
    else:
        print ("use old table")
except Exception, e4:
    print ("Error:creat table server_info ")

try:
    if judge_exist.table_exist(cur,'Log')!=1:
        cur.execute("CREATE TABLE `Log` (`ID`  int PRIMARY KEY AUTO_INCREMENT ,`hostID` int NULL , `级别`  int NULL ,`内容`  varchar(50) NULL ,`日期`  varchar(50) NULL , `备注`  varchar(50) NULL )")
    else:
        print("use old table")
except Exception, e5:
    print("Error:creat Log")


# 数据库mysql插入、修改命令
sql_inserver="insert into server_info values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
sql_inlog="insert into Log values(%s,%s,%s,%s,%s,%s)"
sql_incpu = "insert into cpu_dynamic_info values(%s,%s,%s,%s)"
sql_inmem = "insert into mem_dynamic_info values(%s,%s,%s,%s)"
sql_indisk = "insert into disk_dynamic_info values(%s,%s,%s,%s)"
sql_innetwork="insert into network_dynamic_info values(%s,%s,%s,%s,%s)"

# 修改server_info表，以主机名为索引，防止重复
sql_alter="ALTER TABLE `server_info`ADD UNIQUE INDEX `hostname` (`节点名称`) "
try:
    cur.execute(sql_alter)
except:
    print("已经修改主机名唯一")



start_time = time.time()

hostname_set=set([0])
sql_selectdb="use collection"
sql_table="select * from server_info"
try:
    cur.execute(sql_selectdb)
    cur.execute(sql_table)
    results=cur.fetchall()
    for row in results:
        hostname_set.add(row[1])
except:
    print("Error")

# 循环插入表，1分钟保存一次
while True:
    # 磁盘信息
    disk_used_info = disk_used.get_disk_used()[1]  # type: unicode
    disk_total = disk_used.get_disk_used()[0]
    # 内存信息
    # memuseinfos=mem_used.get_mem_used().split('\n')
    memtotal=mem_used.get_mem_used()[0]
    memused = mem_used.get_mem_used()[1]
    memtotaltemp=memtotal/1024
    memusedtemp=memused/1024
    memusedtemp2=(memusedtemp/memtotaltemp) * 100
    memory_used="%.2f%%" % ((memusedtemp/memtotaltemp) * 100)
    memory_total="%.2f" % (memtotaltemp)

    # cpu利用率
    cpuinfo = cpu_used.get_cpu_used().split('\n')[2]
    cpuinfo_tmp = cpuinfo.split(' ')
    cpu_used_tmp = "%.2f%%" % (float(cpuinfo_tmp[0]) )

    # 负载信息
    load = Average_load.aver_load().split(' ')
    load1s = load[0] + '%'
    load5s = load[1] + '%'
    load15s = load[2] + '%'

    # cpu核数和型号
    cpu_info2=get_cpuinfo.getCpu()

    cpu_num=cpu_info2[0]
    cpu_model=cpu_info2[1]

    (rec_speed,tran_speed)=network_speed.get_rxandtx()
    # tran_speed=network_speed.get_rxandtx()[1]

    # 录入时间
    now = time.asctime()



    #ip信息，，ip地址和主机名
    host_ipadd=host_ip.get_netcard()
    host_name= socket.gethostname()

    # 判断记录是否存在，不存在则插入，存在则更新
    if host_name in hostname_set:
        time_update = time.asctime()
        # print time_update
        sql_update = "UPDATE  server_info " \
                     "SET  内存='"+str(memory_total)+"G', `磁盘空间`='"+str(disk_total)+"G', `修改时间`=\'"+time_update+"\'  WHERE `节点名称` = \'"+host_name+"\'"
        cur.execute(sql_update)
    else:
        cur.execute(sql_inserver, (0, host_name, host_ipadd, "DataNode", cpu_model, cpu_num, str(memory_total) + "G", str(disk_total) + "G", now, now, 1,"NULL"))
        hostname_set.add(host_name)

    #动态表的host_id 和服务器表的ID绑定
    sql_table2 = "select * from server_info where `节点名称`=\'"+host_name+"\'"
    # sql_table2 = "select * from server_info where `节点名称`='ubantu'"
    flag=0
    try:
        cur.execute(sql_selectdb)
        cur.execute(sql_table2)
        results = cur.fetchone()
        host_id=results[0]
        flag=1
    except:
        print("Error: not find hostname in server_info")
        print("Please insert imformation about this server!")



    # 执行mysql命令,插入各表,,server_info中若存在此服务器则统计此服务器的信息，否则将服务器不存在,或者主机名错误的结果上报到日志表
    if flag==1:
        cur.execute(sql_indisk, (0,host_id,str(disk_used_info)+'%', now))
        cur.execute(sql_inmem, (0,host_id, memory_used, now))
        cur.execute(sql_incpu, (0,host_id, cpu_used_tmp, now))
        cur.execute(sql_innetwork,(0,host_id,str(rec_speed)+'kB/s',str(tran_speed)+'kB/s',now))
        if memusedtemp2>=50:
            cur.execute(sql_inlog, (0,host_id,2,"memory is used beyond 50%",now,"Warning"))
        if float(disk_used_info)>=50.0:
            cur.execute(sql_inlog, (0,host_id,2,"disk is used beyond 50%",now,"Warning"))
        if float(cpuinfo_tmp[0])>=50:
            cur.execute(sql_inlog, (0, host_id, 2, "cpu is used beyond 50%", now, "Warning"))
        if memusedtemp2>=80:
            cur.execute(sql_inlog, (0,host_id,3,"memory is used beyond 80%",now,"Error"))
        if float(disk_used_info) >=80.0:
            cur.execute(sql_inlog, (0,host_id,3,"disk is used beyond 80%",now,"Error"))
        if float(cpuinfo_tmp[0])>=80:
            cur.execute(sql_inlog, (0, host_id, 3, "cpu is used beyond 80%", now, "Error"))
    else:
        cur.execute(sql_inlog, (0, "NULL",1,'Not find server:'+host_name,now,'NULL'))


    # cur.execute(sql_in, ("Average_load(1s)", load1s, now))
    # cur.execute(sql_in, ("Average_load(5s)", load5s, now))
    # cur.execute(sql_in, ("Average_load(15s)", load5s, now))

    conn.commit()

    print "saving....."
    time.sleep(60)           ##fresh per 60 second
    # end_time = time.time()
    # if end_time - start_time >= 30:
    #     selc = raw_input("Data stored for 30 seconds has been stored,continue?(Y/N)")
    #     if selc.lower() == "y":
    #         start_time = time.time()
    #         continue
    #     else:
    #         break


# 关闭游标和数据库
cur.close()
conn.close()
