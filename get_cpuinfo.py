from subprocess import Popen, PIPE
def getCpu():
    num = 0
    with open('/proc/cpuinfo') as fd:
        for line in fd:
            if line.startswith('processor'):
                num += 1
            if line.startswith('model name'):
                cpu_model = line.split(':')[1].strip().split()
                cpu_model = cpu_model[0] + ' ' + cpu_model[2] + ' ' + cpu_model[-1]
    return (num,cpu_model)
if __name__ == '__main__':
    print getCpu()

