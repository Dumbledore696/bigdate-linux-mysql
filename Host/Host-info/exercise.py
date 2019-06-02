import re
import pymysql
import conf
conn = pymysql.connect(user=conf.user, passwd=conf.passwd, host=conf.host, port=conf.port)
cur = conn.cursor()
# cur.execute(sql1)
# cur.execute(sql)
sql = "show databases"
cur.execute(sql)
databases = [cur.fetchall()]
database_list = re.findall('(\'.*?\')', str(databases))
database_list2=[re.sub("'",'',each) for each in database_list]
print databases
print database_list
print database_list2
pattern=re.compile('[a-z]|[A-Z]')
m=pattern.findall("ruByrub2e#ahha")
s='I have a dog ,I have a cat'
m=re.findall(r'I have a (?:dog|cat)',s)
s='123 321\n456 654\n789 987'
m=re.findall('\S','a b  \n c')
s='ababAb\nabbabb aabaab'
m=re.findall(r'\w''(?i)',s)

s=r'23455hkihk67868  797908 '
m=re.findall('^([0-9]+)$',s)
print m
