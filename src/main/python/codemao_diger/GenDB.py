import sqlite3
import sys

args=sys.argv[1:]
try:
    connection=sqlite3.connect(args[0])
    cursor=connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS posts(id INT PRIMARY KEY,title TEXT,content TEXT,user_id TEXT,user_nickname TEXT,board_id INT,board_name TEXT,n_views INT,n_replies INT,n_comments INT);")
    cursor.execute("CREATE TABLE IF NOT EXISTS noExistPosts(id INT PRIMARY KEY);")
    connection.commit()
except IndexError:
    print("传参有误：正确顺序为:[数据库URL]")