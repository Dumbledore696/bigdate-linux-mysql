import os
def get_mem_used():
    # f = os.popen("free -m |grep Mem |awk '{print $2,$3}'")
    f=os.popen("cat /proc/meminfo | sed '2d' | awk 'NR==1,NR==2 {print $2}'")
    return f.read()