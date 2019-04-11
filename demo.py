from __future__ import division
import pymysql
import time, conf
import disk_used, mem_used, cpu_used, Average_load

conn = pymysql.connect(user=conf.user, passwd=conf.passwd, host=conf.host, port=conf.port)
cur = conn.cursor()

try:
    cur.execute("create database disk_used_db")
except Exception, e:
    choise = raw_input("database disk_used_db exists,drop? (Y/N)")
    if choise.lower() == "y":
        cur.execute("drop database disk_used_db")
        cur.execute("create database disk_used_db")
        print "drop old database and creating new database(disk_used_db)... "
        time.sleep(1)
        print "creat new database success!!"
    else:
        print "used old database"
conn.select_db("disk_used_db")
try:
    cur.execute("create table disk_used_info(name varchar(20),status varchar(30),mytime varchar(50))")
except Exception, e1:
    choise1 = raw_input("table disk_used_info exists,drop? (Y/N)")
    if choise1.lower() == "y":
        cur.execute("drop table disk_used_info")
        cur.execute("create table disk_used_info(name varchar(20),status varchar(30),mytime varchar(50))")
        print "drop old table and creating new table(disk_used_info)... "
        time.sleep(1)
        print "creat new table success!!"
    else:
        print "used old table"
# sql_in = "insert into disk_used_info values(%s,%s,%s)"
# start_time = time.time()
# while True:
#
#     disk_used_info = disk_used.get_disk_used().strip()
#
#     memuseinfos = mem_used.get_mem_used().split('\n')
#     memtotal = memuseinfos[0]
#     memavailable = memuseinfos[1]
#     memtotaltemp = float(memtotal) / 1024 / 1024
#     memavailabletemp = float(memavailable) / 1024 / 1024
#     memusedtemp = memtotaltemp - memavailabletemp
#     memory_used = "%.2f%%" % ((memusedtemp / memtotaltemp) * 100)
#
#     cpuinfo = cpu_used.get_cpu_used().split('\n')[2]
#     cpuinfo_tmp = cpuinfo.split(' ')
#
#     cpu_used_tmp = "%.2f%%" % (float(cpuinfo_tmp[0]))
#
#     load = Average_load.aver_load().split(' ')
#     load1s = load[0] + '%'
#     load5s = load[1] + '%'
#     load15s = load[2] + '%'
#
#     now = time.asctime()
#     cur.execute(sql_in, ("disk_used", disk_used_info + '%', now))
#     cur.execute(sql_in, ("mem_used", memory_used, now))
#     cur.execute(sql_in, ("cpu_used", cpu_used_tmp, now))
#     cur.execute(sql_in, ("Average_load(1s)", load1s, now))
#     cur.execute(sql_in, ("Average_load(5s)", load5s, now))
#     cur.execute(sql_in, ("Average_load(15s)", load5s, now))
#
#     conn.commit()
#     print "saving....."
#     time.sleep(5)  ##fresh per 5 second
#     end_time = time.time()
#     if end_time - start_time >= 30:
#         selc = raw_input("Data stored for 30 seconds has been stored,continue?(Y/N)")
#         if selc.lower() == "y":
#             start_time = time.time()
#             continue
#         else:
#             break

cur.close()
conn.close()
