from .Requester import Requester
from ..DBMapper.NoExistPostsMapper import NoExistPostsMapper
from ..DBMapper.PostMapper import PostMapper
import logging
import time

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

class Program:
    def __init__(self,start_id,end_id,sleep_time,db_url):
        self.requester=Requester("https://api.codemao.cn/web/forums/posts/{}/details",'db/data.db')
        self.db_url=db_url
        self.noExistPostMapper=NoExistPostsMapper(self.db_url)
        self.postMapper=PostMapper(self.db_url)
        self.start_id=start_id
        self.end_id=end_id
        self.sleep_time=sleep_time
        self.logger=logging.getLogger(__name__)
        
    def doJob(self):
        for i in range(self.start_id,self.end_id+1):
            if not(self.noExistPostMapper.isExistById(i) or self.postMapper.isPostExistById(i)):
                res=self.requester.requestById(i)
                if res.status=="FAILURE":
                    self.noExistPostMapper.addNoExist(res.id)
                    self.logger.info(f'request id {i},fail')
                elif res.status=="OK":
                    self.postMapper.addPost(res.id,res.title,res.content,res.user_id,res.user_nickname,res.board_id,res.board_name,res.n_views,res.n_replies,res.n_comments)
                    self.logger.info(f'request to {i},PostEntity:{res}')
                time.sleep(self.sleep_time)
            else:
                self.logger.info(f"id {i} is exist in db,skipped")