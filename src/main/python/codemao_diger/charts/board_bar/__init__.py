from codemao_diger.DBMapper.PostMapper import PostMapper
from pyecharts.charts import Bar
from collections import Counter
from codemao_diger.charts.board_bar.BoardEntity import BoardEntity

class BoardBar(Bar):
    def __init__(self,db_url,output_file):
        super().__init__()
        self.db_url=db_url
        self.output_file=output_file
        self.x_axis=[]
        self.y_axis=[]
        self.postMapper=PostMapper(self.db_url)
        
    def genCount(self):
        res=self.postMapper.getAllBoardName()
        boardsData=[]
        for i in res:
            boardsData.append(i[0])
        counter=Counter(boardsData)
        boards=[]
        for i in counter:
            boards.append(BoardEntity(i,counter[i]))
        boards=sorted(boards,key=lambda x:x.post_count,reverse=True)
        for i in boards:
            self.x_axis.append(i.board_name)
            self.y_axis.append(i.post_count)
    def render(self):
        self.genCount()
        self.add_xaxis(self.x_axis)
        self.add_yaxis("帖子数量",self.y_axis)
        super().render(self.output_file)
