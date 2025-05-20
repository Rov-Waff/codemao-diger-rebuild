# Request.py -- 只是为了找第一个帖子
import requests,time

if __name__=='__main__':
    url='https://api.codemao.cn/web/forums/posts/{}/details' #{}是Python的占位符
    id=1
    while(True):
        res=requests.get(url.format(id)) #格式化字符串，说白了就是把占位符占的位置填回去
        print("Request:url:{}".format(url.format(id)))
        if(res.status_code==200):
            print("Found!URL:{}".format(url.format(id)))
            break
        id+=1
        time.sleep(0.1) #之前看到过洛谷上有同学爬虫不写sleep把洛谷服务器爬宕机了，不写这句就是想把猫站爬宕机（