# HuhSQLite.py - SQLite是啥？能吃吗
import sqlite3

connection = sqlite3.connect('example.db') # 创建连接，连接到数据库，如果没有这个数据库文件就创建它
cursor=connection.cursor() #创建游标用于操作数据库

# cursor.execute() 执行SQL语句，括号里写SQL语句
cursor.execute('CREATE TABLE IF NOT EXISTS grade(id INT PRIMARY KEY,name TEXT,chinese INT,math INT,total INT);') #向数据库里创建grade表,前提该表不存在，表里有五个列，分别为id,name,chinese,math,total
connection.commit() #涉及修改数据库的操作要用这行代码提交

cursor.execute('INSERT INTO grade VALUES(?,?,?,?,?)',(3,"张三",100,100,200)) #向grade表里插入数据，?为sqlite3中SQL语句的占位符，第二个参数为一个元组或列表，从做到后占回SQL语句中的占位符
connection.commit()

cursor.execute('SELECT * FROM grade WHERE id=?',(1,))#查询grade表里的id为1的所有数据,不写WHERE条件就是查询整张表
print(cursor.fetchall())