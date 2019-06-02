# encoding: utf-8
from __future__ import division
import sys
#sys.path.append('/./home/njit/PycharmProjects/Host/venv/lib/python2.7/site-packages')
sys.path.append('/./home/Host/venv/lib/python2.7/site-packages')

import  os
import commands
import pymysql,psutil
import time, conf
import socket
def get_disk_used():
#now = time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(time.time()))
#a=psutil.disk_usage('/')
#print a
	total=psutil.disk_usage('/').total/1024/1024/1024
	used=psutil.disk_usage('/').used/1024/1024/1024
	sum2=('%.2f') % total
	percent=("%.2f")%((used/total)*100)
	print sum2
	print percent
if __name__ == '__main__':
	get_disk_used() 
#mount=commasmount = commands.getoutput('mount -v')  
#lines = mount.split('\n')  
#points = map(lambda line: line.split()[2], lines)  
#total=0  
#used=0  
#for i in points:  
#	total+=float(psutil.disk_usage(i).total)  
#	used+=float(psutil.disk_usage(i).used)  
#total=total/1024/1024/1024  
#used=used/1024/1024/1024  
#tot=('%.2f')%total  
#percent=("%.2f")%((used/total)*100)  
#print percent
#print tot
#print used
