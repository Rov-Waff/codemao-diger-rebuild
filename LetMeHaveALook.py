# LetMeHaveALook.py - 让我看看你的响应体里有什么

import requests
import json

if __name__=="__main__":
    id=int(input())
    res=requests.get("https://api.codemao.cn/web/forums/posts/{}/details".format(id))
    print(content['title'])