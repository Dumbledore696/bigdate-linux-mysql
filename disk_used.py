# encoding: utf-8
#root下才能出结果
import commands
import  psutil
def get_disk_used():

    mount = commands.getoutput('mount -v')
    lines = mount.split('\n')
    points = map(lambda line: line.split()[2], lines)
    total=0
    used=0
    for i in points:
        total+=float(psutil.disk_usage(i).total)
        used+=float(psutil.disk_usage(i).used)

    total=total/1024/1024/1024
    used=used/1024/1024/1024
    tot=('%.2f')%total
    percent=("%.2f")%((used/total)*100)
    return (tot,percent)
# if __name__ == '__main__':
#     print get_disk_used()[1]
#     print str(get_disk_used()[0])
