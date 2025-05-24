import requests,json
from .entity.PostEntity import PostEntity

class Requester:
    def __init__(self,url,db_path):
        self.url=url
        self.db_path=db_path
        
    def isPostExistOnlineById(self,id):
        res=requests.get(self.url.format(id))
        if res.status_code==200:
            return True
        else:
            return False
        
    def requestById(self,id):
        res=requests.get(self.url.format(id))
        if self.isPostExistOnlineById(id):
            res_content=json.loads(res.content)
            post_id=int(res_content['id'])
            title=res_content['title']
            content=res_content['content']
            user_id=int(res_content['user']['id'])
            user_nickname=res_content['user']['nickname']
            board_id=int(res_content['board_id'])
            board_name=res_content['board_name']
            n_views=int(res_content['n_views'])
            n_replies=int(res_content['n_replies'])
            n_comments=int(res_content['n_comments'])
            return PostEntity('OK',post_id,title,content,user_id,user_nickname,board_id,board_name,n_views,n_replies,n_comments)
        
        else:
            return PostEntity('FAILURE',id,'','',0,'',0,'',0,0,0)
        
if __name__=='__main__':
    requester=Requester("https://api.codemao.cn/web/forums/posts/{}/details","db/data.db")
    print(requester.requestById(3))
    print(requester.requestById(72))
    