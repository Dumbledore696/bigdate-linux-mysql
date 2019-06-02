import os

def get_disk_used():
    f=os.popen("df -h | sed '1d' | awk '{sum += $5};END {print sum}'")
    return f.read()