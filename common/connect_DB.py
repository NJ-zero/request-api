#coding=utf-8
#author='Shichao-Dong'
import psycopg2
import configparser
import readConfig as conf



host = conf.ReadConfig().getdbConfigValue('host')
port = conf.ReadConfig().getdbConfigValue('port')
user = conf.ReadConfig().getdbConfigValue('user')
password = conf.ReadConfig().getdbConfigValue('password')
db = conf.ReadConfig().getdbConfigValue('db_name')

# =============封装数据库基本操作================
class DB :

    def __init__(self):
        try:
            self.conn = psycopg2.connect(host= host ,
                                         user=user,
                                         port=port,
                                         password=password,
                                         database=db,
                                         )
        except Exception as e:
            print e

    def select(self,sql):
        cusor = self.conn.cursor()
        cusor.execute(sql)
        rows = cusor.fetchall()
        # for row in rows:
        #     print row[0]
        return rows[0][0]

    def close(self):
        self.conn.close()

