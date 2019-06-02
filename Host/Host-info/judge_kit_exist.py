import  sys
import os
f=os.popen("ps -ef | grep  python").read().split()

# print f.split()
if 'main.py' in f:
    print 1
else:
    print 0