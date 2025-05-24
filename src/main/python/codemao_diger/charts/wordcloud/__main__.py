import sys
from codemao_diger.charts.wordcloud import HotWordCloud

try:
    args=sys.argv[1:]
    postBar=HotWordCloud(args[0],args[1])
    postBar.render()
except IndexError:
    print("传参有误，顺序为:[数据库URL] [生成图表URL]")