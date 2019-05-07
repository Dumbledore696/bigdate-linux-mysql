# encoding: utf-8
from __future__ import division
import sys
sys.path.append('/./home/hadoop/Host/venv/lib/python2.7/site-packages')
import  os
import time
import socket
import pymysql
import conf,judge_exist
#def get_hadoop_errorlog():
#对日志存放的路径有要求
conn = pymysql.connect(user=conf.user, passwd=conf.passwd, host=conf.host, port=conf.port)
cur = conn.cursor()
try:
    if judge_exist.table_exist(cur,'hadoop_log')!=1:
        cur.execute("CREATE TABLE `hadoop_log` (`id`  int PRIMARY KEY AUTO_INCREMENT ,`hostID` int NULL,`content`  varchar(255) NULL ,`level`  varchar(50) NULL ,`create_time`  datetime NULL ,`update_time` datetime NULL , `date` date NULL)")
    else:
        print ("use old table")
except Exception, e1:
    print ("Error:creat table hadoop_log ")
host_name= socket.gethostname()
now2 = time.strftime('%Y-%m-%d', time.localtime(time.time()))

sql_inhadoop="insert into hadoop_log values(%s,%s,%s,%s,%s,%s,%s)"
sql_selectdb="use collection"
sql_table2 = "select * from server_info where `equip_name`=\'"+host_name+"\'"

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


now=time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time()))
nowdate=time.strftime('%Y.%m.%d',time.localtime(time.time()))
hname=socket.gethostname()

if hname=='master':
	f1=os.popen('cat /./usr/local/hadoop/logs/hadoop-hadoop-namenode-'+hname+'.log').read().split('\n')
	f2=os.popen('cat /./usr/local/hadoop/logs/hadoop-hadoop-secondarynamenode-'+hname+'.log').read().split('\n')
	f3=os.popen('cat /./usr/local/hadoop/logs/yarn-hadoop-resourcemanager-'+hname+'.log').read().split('\n')
	for line in f3:
		if now2 in line:
			t=time.localtime(time.time()-3000)
			t2=time.localtime(time.time())
			tfore5=time.strftime("%Y-%m-%d %H:%M:%S", t).split(' ')#5分钟前的时间
			now_time=time.strftime("%Y-%m-%d %H:%M:%S", t2).split(' ')#现在的时间
			linesplit=line.split(' ')
			
			if linesplit[1].split(',')[0]<=now_time[1] and linesplit[1].split(',')[0]>=tfore5[1]:
				#if 'WARN' or 'ERROR'in line:
				if 'INFO' in line:
					cur.execute(sql_inhadoop,(0,host_id,line,"earn",now,now,nowdate))
		else:
			print error
else:
	f1=os.popen('cat /./usr/local/hadoop/logs/hadoop-hadoop-datanode-'+hname+'.log').read().split('\n')
	f2=os.popen('cat /./usr/local/hadoop/logs/yarn-hadoop-nodemanager-'+hname+'.log').read().split('\n')
for line in f1:
	if now2 in line:
		t=time.localtime(time.time()-300)
		t2=time.localtime(time.time())
		tfore5=time.strftime("%Y-%m-%d %H:%M:%S", t).split(' ')#5分钟前的时间
		now_time=time.strftime("%Y-%m-%d %H:%M:%S", t2).split(' ')#现在的时间
		linesplit=line.split()
		
		if linesplit[1].split(',')[0]<=now_time[1] and linesplit[1].split(',')[0]>=tfore5[1]:
			#if 'WARN' or 'ERROR'in line:
			if 'INFO' in line:
				cur.execute(sql_inhadoop,(0,host_id,line,'warn',now,now,nowdate))
for line in f2:
	if now2 in line:
		t=time.localtime(time.time()-300)
		t2=time.localtime(time.time())
		tfore5=time.strftime("%Y-%m-%d %H:%M:%S", t).split(' ')#5分钟前的时间
		now_time=time.strftime("%Y-%m-%d %H:%M:%S", t2).split(' ')#现在的时间
		linesplit=line.split(' ')
		
		if linesplit[1].split(',')[0]<=now_time[1] and linesplit[1].split(',')[0]>=tfore5[1]:
			if 'INFO' in line:
				cur.execute(sql_inhadoop,(0,host_id,line,'warn',now,now,nowdate))
		
conn.commit()
cur.close()
conn.close()










