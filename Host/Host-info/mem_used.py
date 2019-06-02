import os
def get_mem_used():
    f=os.popen("free -m | sed '1d' | awk 'NR==1 {print $2,$3}' ")
    l=f.read().split()
    used=l[1]
    total=l[0]
    used=float(used)
    total=float(total)
    return (total,used)
