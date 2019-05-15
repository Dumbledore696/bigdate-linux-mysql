#encoding: utf-8
#root下才能出结果
import commands
import os
import  psutil
def get_disk_used():
	total=psutil.disk_usage('/').total/1024/1024/1024
    used=psutil.disk_usage('/').used/1024/1024/1024
    sum= ('%.2f') % total
    percent=("%.2f")%((used/total)*100)
    #f = os.popen("fdisk -l").readlines()
    #sum = 0
    # print f
    #for line in f:
    #    if (line.startswith('Disk /dev/sda:')) or (line.startswith('Disk /dev/sdb:')):
    #        sum += float(line.split()[2])#只能用float强制转型，因为字符串中有小数点
    #mount = commands.getoutput('mount -v')
    #lines = mount.split('\n')
    #map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回
    #points = map(lambda line: line.split()[2], lines)
    #total=0
    #used=0
    #for i in points:
    #    total+=float(psutil.disk_usage(i).total)
    #    used+=float(psutil.disk_usage(i).used)

    #total=total/1024/1024/1024
    #used=used/1024/1024/1024
    #tot=('%.2f')%total
    #percent=("%.2f")%((used/total)*100)
    return (sum,percent)
# if __name__ == '__main__':
#     print get_disk_used()[1]
#     print str(get_disk_used()[0])
# print psutil.disk_usage('/')
