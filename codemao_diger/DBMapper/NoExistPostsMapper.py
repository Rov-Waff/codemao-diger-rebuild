import sqlite3

class NoExistPostsMapper:
    def __init__(self,db_path):
        self.db_path=db_path
        self.connection=sqlite3.connect(self.db_path)
        self.cursor=self.connection.cursor()
        
    def isExistById(self,id):
        self.cursor.execute("SELECT * FROM noExistPosts WHERE id=?",(id,))
        if self.cursor.fetchall()==[]:
            return False
        else: 
            return True
        
    def addNoExist(self,id):
        self.cursor.execute("INSERT INTO noExistPosts VALUES(?)",(id,))
        self.connection.commit()
        
    def getAll(self):
        self.cursor.execute("SELECT * FROM noExistPosts")
        return self.cursor.fetchall()
        
if __name__=="__main__":
    noExistPostsMapper=NoExistPostsMapper("db/data.db")
    noExistPostsMapper.addNoExist(1)
    print(noExistPostsMapper.isExistById(1))
    print(noExistPostsMapper.getAll())