import sys
from codemao_diger.charts.post_bar import PostBar

try:
    args=sys.argv[1:]
    postBar=PostBar(args[0],int(args[1]),args[2])
    postBar.render()
except IndexError:
    print("传参有误，顺序为:[数据库URL] [X轴数量] [生成图表URL]")