from . import Program
import sys

args = sys.argv[1:]
try:
    program=Program(int(args[0]),int(args[1]),float(args[2]),args[3])
    program.doJob()
except IndexError:
    print('传参不正确，顺序为:[起始id] [结束id] [间隔时间] [数据库URL]')