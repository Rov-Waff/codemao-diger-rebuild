import sqlite3
import sys

def generate_db(url):
    connection=sqlite3.connect(url)
    cursor=connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS posts(id INT PRIMARY KEY,title TEXT,content TEXT,user_id TEXT,user_nickname TEXT,board_id INT,board_name TEXT,n_views INT,n_replies INT,n_comments INT);")
    cursor.execute("CREATE TABLE IF NOT EXISTS noExistPosts(id INT PRIMARY KEY);")
    connection.commit()

args=sys.argv[1:]
try:
    generate_db(args[0])
    print(f"成功生成帖子数据库到{args[0]}")
except IndexError:
    print("传参有误：正确顺序为:[数据库URL]")
except:
    print("因为未知原因无法生成")