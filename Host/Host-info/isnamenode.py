# encoding: utf-8
from __future__ import division

import  os
def judge_namenode():
    try:
        f=os.popen('jps').read().split()
        if 'NameNode' in f:
            return 'NameNode'
        else:
            return 'DateNode'
        # print f
    except:
        return 'DateNode'
#root下没有jps命令，所以在root下下载jdk：apt-get install openjdk-8-jdk-headless




