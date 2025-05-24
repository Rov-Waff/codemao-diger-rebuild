class PostEntity:
    def __init__(self,status,id,title,content,user_id,user_nickname,board_id,board_name,n_views,n_replies,n_comments):
        self.status=status
        self.id=id
        self.title=title
        self.content=content
        self.user_id=user_id
        self.user_nickname=user_nickname
        self.board_id=board_id
        self.board_name=board_name
        self.n_views=n_views
        self.n_replies=n_replies
        self.n_comments=n_comments
    
    def __str__(self):
        return f"ResponseEntity(status={self.status},id={self.id},title={self.content},user_id={self.user_id},user_nickname={self.user_nickname},board_id={self.board_id},board_name={self.board_name},n_views={self.n_views},n_replies={self.n_replies},n_comments={self.n_replies})"