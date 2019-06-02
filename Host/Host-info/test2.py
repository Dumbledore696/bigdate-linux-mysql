import sys
sys.path.append('/./home/Host/venv/lib/python2.7/site-packages')
import commands
import  psutil
mount = commands.getoutput('mount -v')
lines = mount.split('\n')
points = map(lambda line: line.split()[2], lines)
b=0
for i in points:
    b+=float(psutil.disk_usage(i).total)

b2=b/1024/1024/1024
print ('%.2f')%b2
# print len(points)
# print points
