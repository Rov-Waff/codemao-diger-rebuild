from codemao_diger.charts.board_bar import BoardBar
import sys

args=sys.argv[1:]
try:
    postBar=BoardBar(args[0],args[1])
    postBar.render()

except IndexError:
    print("传参错误，正确顺序为:[数据库URL] [输出文件URL]")