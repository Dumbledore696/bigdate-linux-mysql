import time
import os
disk_total = os.popen("df -h | sed '1d' | awk '{sum += $2};END {print sum}'").read()
s=time.asctime()
print(type(s))
print(type(disk_total))
