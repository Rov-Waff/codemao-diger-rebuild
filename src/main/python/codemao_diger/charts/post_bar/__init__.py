from pyecharts.charts import Bar
import sqlite3
from codemao_diger.DBMapper.PostMapper import PostMapper
from collections import Counter
from codemao_diger.charts.post_bar.UserEntity import UserEntity

class PostBar(Bar):
    def __init__(self,db_url,ranktop,path):
        super().__init__()
        self.connection=sqlite3.connect(db_url)
        self.cursor=self.connection.cursor()
        self.postMapper=PostMapper(db_url)
        self.db_url=db_url
        self.x_axis=[]
        self.y_axis=[]    
        self.ranktop=ranktop
        self.path=path
    
    def genCount(self):
        res=self.postMapper.getAllUserID()
        uid_list=[]
        for i in res:
            uid_list.append(i[0])
        counter=Counter(uid_list)
        userList=[]
        for i in counter:
            userList.append(UserEntity(int(i),'',counter[i],self.db_url))
        for i in userList:
            i.reload_username()
        sorted_userList=sorted(userList,key=lambda x:x.n_post,reverse=True)
        for i in sorted_userList:
            self.x_axis.append(i.username)
            self.y_axis.append(i.n_post)
    def render(self):
        self.genCount()
        self.add_xaxis(self.x_axis[:self.ranktop])
        self.add_yaxis("发帖量",self.y_axis[:self.ranktop])
        return super().render(self.path)