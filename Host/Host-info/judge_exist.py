# import pymysql
import  re
# import conf
# conn = pymysql.connect(user=conf.user, passwd=conf.passwd, host=conf.host, port=conf.port)
# cur = conn.cursor()
# # cur.execute(sql1)
# # cur.execute(sql)

def database_exist(cur,database_name):
    sql = "show databases"
    cur.execute(sql)
    databases=[cur.fetchall()]
    database_list=re.findall('(\'.*?\')',str(databases))
    database_list=[re.sub("'",'',each) for each in database_list]
    if database_name in database_list:
        return 1
    else:
        return 0

def table_exist(cur,table_name):
    sql1="use collection"
    sql="show tables"
    cur.execute(sql1)
    cur.execute(sql)
    tables = [cur.fetchall()]
    table_list = re.findall('(\'.*?\')', str(tables))
    table_list= [re.sub("'", '', each) for each in table_list]
    if table_name in table_list:
        return 1
    else:
        return 0

# table_name='Log'
# database_name='disk_used_db'



