from pyecharts.charts import WordCloud
from codemao_diger.DBMapper.PostMapper import PostMapper
import jieba
from bs4 import BeautifulSoup
from collections import Counter

class HotWordCloud(WordCloud):
    def __init__(self, db_url,output_file):
        super().__init__()
        self.db_url=db_url
        self.output_file=output_file
        self.postMapper=PostMapper(self.db_url)
        self.word_pair=[]
        
    
    def genWordPair(self):
        words=[]
        res=self.postMapper.getAllTitleAndContent()
        for i in res:
            title_words=jieba.cut(i[0])
            soup=BeautifulSoup(i[1],'html.parser')
            content_words=jieba.cut(soup.get_text())
            for i in title_words:
                if len(i)>1:
                    words.append(i)
            for i in content_words:
                if len(i)>1:
                    words.append(1)
        counter=Counter(words)
        for i in counter:
            self.word_pair.append((i,counter[i]))
    
    def render(self):
        self.genWordPair()
        super().add(series_name='热词统计',data_pair=self.word_pair)
        super().render(self.output_file)
        
if __name__=='__main__':
    hotWordCloud=HotWordCloud("/home/seterain3913/文档/codemao-diger-rebuild/db/data.db","/home/seterain3913/文档/codemao-diger-rebuild/db/render.html")
    hotWordCloud.render()