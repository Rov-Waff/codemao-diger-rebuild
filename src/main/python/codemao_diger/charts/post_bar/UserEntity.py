from codemao_diger.DBMapper.PostMapper import PostMapper

class UserEntity:
    def __init__(self,id,username,n_post,db_url):
        self.id=id
        self.username=username
        self.n_post=n_post
        self.postMapper=PostMapper(db_url)
        
    def reload_username(self):
        self.username=self.postMapper.getUsernameById(self.id)
        
        
if __name__=='__main__':
    user=UserEntity(1,'',10,'/home/seterain3913/文档/codemao-diger-rebuild/db/data.db')
    user.reload_username()
    print(user.username)