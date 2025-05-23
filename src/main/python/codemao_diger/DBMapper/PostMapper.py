import sqlite3

class PostMapper:
    def __init__(self,db_path):
        self.db_path=db_path
        self.connection=sqlite3.connect(self.db_path)
        self.cursor=self.connection.cursor()
        
    def setPath(self,db_path):
        self.db_path=db_path
        self.__init__()
        
    def getAll(self):
        self.cursor.execute("SELECT * FROM posts")
        return self.cursor.fetchall()
    
    def addPost(self,id,title,content,user_id,user_nickname,board_id,board_name,n_views,n_replies,n_comment):
        self.cursor.execute("INSERT INTO posts VALUES(?,?,?,?,?,?,?,?,?,?)",(id,title,content,user_id,user_nickname,board_id,board_name,n_views,n_replies,n_comment))
        self.connection.commit()
        
    def isPostExistById(self,id):
        self.cursor.execute("SELECT * FROM posts WHERE id=?",(id,))
        if self.cursor.fetchall()==[]:
            return False
        else:
            return True
        
        
if __name__=="__main__":
    postMapper = PostMapper("db/data.db")
    postMapper.addPost(1,'test','test',1,'test',1,'test',1,1,1)
    print(postMapper.getAll())
    print(postMapper.isPostExistById(1))