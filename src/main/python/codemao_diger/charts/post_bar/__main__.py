import sys
from codemao_diger.charts.post_bar import PostBar

args=sys.argv[1:]
postBar=PostBar(args[0],int(args[1]),args[2])
postBar.render()