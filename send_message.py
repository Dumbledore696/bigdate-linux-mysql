# -*- coding: utf-8 -*-
'''
发送错误日志,,qq邮箱需要开启smtp服务，然后得到授权码，这个作为口令
'''
import os
import smtplib
import time
import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def send_mail(to_list, sub, content):  # to_list：收件人；sub：主题；content：邮件内容
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "1362371931@qq.com"  # 用户名
    mail_pass = "kbwvurkebxotjbag"  # 口令
    mail_postfix = "qq.com"  # 发件箱的后缀

    me = "错误日志" + "<" + mail_user + "@" + mail_postfix + ">"  # 这里的hello可以任意设置，收到信后，将按照设置显示
    msg = MIMEMultipart()
    msg['Subject'] = sub  # 设置主题
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    # ---邮件正文---
    part = MIMEText(open(objectdir, 'r').read(), _charset='gb2312')  # 将错误文件内容做为邮件正文内容
    msg.attach(part)

    # txt类型附件
    part = MIMEApplication(open(objectdir, 'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename="error_log.txt")
    msg.attach(part)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)  # 连接smtp服务器
        s.login(mail_user, mail_pass)  # 登陆服务器
        s.sendmail(me, to_list, msg.as_string())  # 发送邮件
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False


# 获取错误日志内容
def getContent(resouce, final):
    f = os.popen("cat /./var/log/syslog").read().split('\n')
    # print f
    finalfile = open(final, 'w')
    try:
        for line in f:
            if yes_date in line:#确定是今天的日志
                t = time.localtime(time.time() - 300)
                tfore5=time.strftime("%Y-%m-%d %H:%M:%S", t).split(' ')#5分钟前的时间
                now_date = get_update_date()[1]                        #现在的时间

                linesplit=line.split(' ')                              #log中的时间
                if linesplit[2] <=now_date and linesplit[2]>=tfore5[1]:#筛选从上次执行到这次执行5分钟内的日志

                    if  "ERROR" in line:  # 按行读取，如果该行包含“ERORR”字符串，则将该行写入目标文件
                        finalfile.write(line)
                        finalfile.write('\n')
    finally:
        finalfile.close()


# 获取今天的时间，用于字符串匹配
def get_update_date():
    time_update2 = time.asctime().split(' ')
    yes_date=time_update2[1]+' '+time_update2[2]
    now_date=time_update2[3]
    return (yes_date,now_date)


if __name__ == '__main__':
    sourcedir = "/./var/log/syslog"  # 需要读取的源文件路径
    objectdir = "/./home/error_log.txt"  # 存放的目标文件
    mailto_list = ["1362371931@qq.com"]  # 收件人邮箱，可以发送存放多个
    yes_date = get_update_date()[0]      # 得到日期

    getContent(sourcedir, objectdir)
    if os.path.getsize(objectdir):
        today=datetime.datetime.now()
        today = today.strftime("%Y-%m-%d")
        if send_mail(mailto_list, "错误日志_" + today, objectdir):
            print "发送成功"
        else:
            print "发送失败"
    else:
        print "无错误日志，未发送邮件"
