import sqlite3
import sys

def generate_db(url):
    connection=sqlite3.connect(url)
    cursor=connection.cursor()
    with open("src/main/python/codemao_diger/sql/initdb.sql","r")as f:
        sql=f.read().split(";")
        for i in sql:
            cursor.execute(i)
    connection.commit()

args=sys.argv[1:]
try:
    generate_db(args[0])
    print(f"成功生成帖子数据库到{args[0]}")
except IndexError:
    print("传参有误：正确顺序为:[数据库URL]")
except:
    print("因为未知原因无法生成")
    