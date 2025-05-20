import requests
import sqlite3
import json,time

db_connection=sqlite3.connect('data.db')
db_cursor=db_connection.cursor()

#创建数据库连接

def init_db():
    db_cursor.execute("""CREATE TABLE IF NOT EXISTS posts(id INT PRIMARY KEY,title VARCHAR(100),content VARCHAR(10000),user_id INT,user_nickname VARCHAR(50),board_id INT,board_name VARCHAR(50));""")
    db_connection.commit()
    db_cursor.execute("CREATE TABLE IF NOT EXISTS noExistsId(id INT PRIMARY KEY);")
    db_connection.commit()
# 初始化数据库

def insertData(id,title,content,user_id,user_nickname,board_id,board_name):
    db_cursor.execute("INSERT INTO posts VALUES(?,?,?,?,?,?,?);",(id,title,content,user_id,user_nickname,board_id,board_name))
    db_connection.commit()
def searchDBById(id):
    db_cursor.execute("SELECT * FROM posts where id=?",(id,))
    return db_cursor.fetchall()
def addNotExist(id):
   
    db_cursor.execute("INSERT INTO noExistsId VALUES(?);",(id,))
    db_connection.commit()

def isNotExist(id):
    db_cursor.execute("SELECT * FROM noExistsId where id=?",(id,))
    if db_cursor.fetchall()==[]:
        return True
    else:
        return False


if __name__=="__main__":
    init_db()
    start=int(input("起始ID:"))
    end=int(input("结束ID:"))
    sleep_time=float(input("间隔时间"))
    for i in range(start,end+1):
        if searchDBById(i)==[] and isNotExist(i): #防止同一个URL被反复爬取或反复添加
            url = "https://api.codemao.cn/web/forums/posts/{}/details".format(i)
            r=requests.get(url)
            print("request to {}".format(url))
            request_data=json.loads(r.content)
            if r.status_code!=404:
                insertData(int(request_data['id']),request_data['title'],request_data['content'],int(request_data['user']['id']),request_data['user']['nickname'],
                           int(request_data['board_id']),request_data['board_name'])
                print("inserted data:{}".format(request_data))
            else:
                addNotExist(i) #如果这个请求404了，就把这个id添加进不可用id表以放置反复爬取
                print("id{} no data,add to noExists".format(i))
            time.sleep(sleep_time)
    print("JOB HAS DONE......")