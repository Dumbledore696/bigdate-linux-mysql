# encoding: utf-8
from subprocess import Popen, PIPE
def getCpu():
    num = 0
    with open('/proc/cpuinfo') as fd:#python文件读写，，with open 自动调用close
        for line in fd:
            if line.startswith('processor'):
                num += 1
            if line.startswith('model name'):
                cpu_model = line.split(':')[1].strip().split()#strip()移除字符串首尾的特定字符，若没有指定，移除空格和换行符
                cpu_model = cpu_model[0] + ' ' + cpu_model[2] + ' ' + cpu_model[-1]
    return (num,cpu_model)
if __name__ == '__main__':
    print getCpu()

