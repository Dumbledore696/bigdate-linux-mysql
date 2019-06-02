import os
def get_cpu_used():
    f = os.popen("top -bi -n 1| awk '{print $2,$4}'")
    return f.read()