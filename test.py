import time
import os
disk_total = os.popen("df -h | sed '1d' | awk '{sum += $2};END {print sum}'").read()
s=time.asctime()
print(type(s))
print(type(disk_total))
# h='host1'
# s.add(h)
# if "host1"in s:
#     print ("yes")
#     print(type(h))
# else:
#     print("No")