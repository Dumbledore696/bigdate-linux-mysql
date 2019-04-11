import os
def aver_load():
    f = os.popen("cat /proc/loadavg | awk '{print $1,$2,$2}'")
    return f.read().strip()