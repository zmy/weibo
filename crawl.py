#coding=utf-8
from weiboLogin import WeiboLogin
import threading.Thread
from processInfo import ProcessInfo
import weibologin
from saveFile import FileSave
from saveFile import FileSave
userDict={}
userArray=[]
urlInfo="http://weibo.cn/{uid}?vt=4&gsid=3_5bcf0c5bea3f4fc4ffb4d7ce3c47e6a6f54a265b88c8"
urlFollow="http://weibo.cn/{uid}/follow?page={page}&vt=4&gsid=3_5bcf0c5bea3f4fc4ffb4d7ce3c47e6a6f54a265b88c8"
urlFans="http://weibo.cn/{uid}/fans?page={page}vt=4&gsid=3_5bcf0c5bea3f4fc4ffb4d7ce3c47e6a6f54a265b88c8"
urlTag="http://weibo.cn/account/privacy/tags/?uid={uid}&gsid=3_5bcf0c5bea3f4fc4ffb4d7ce3c47e6a6f54a265b88c8"

class Crawl(threading.Thread):
    def __int__(self,name,username,password):
        threading.Thread.__init__(self)
        self.name=name
        self.weibo=WeiboLogin(self.username,self.password)
        self.process=ProcessInfo()
        self.fileSave=FileSave('\content')
    def userAdd(self,level):
        for k in self.process.userarray:
            if(not userDict.has_key(k)):
                userDict[k]=1
                userArray.append((k,level+1)) 
    def saveUser(self,uid,level):
        str=""
        for k in self.process.info:
            str+=self.process.info
             
    def run(self):
        self.weibo.login()
        while(len(userArray)):
                user=userArray.pop(0)
                uid=user[0]
                level=user[1]
                text=self.weibo.crawlPage(urlInfo.format(uid=uid))
                self.process.clear()
                self.process.init()
                self.process.feed(text)
                
                text=self.weiboCrawlPage(urlFollow.format(uid=uid,page=1))
                self.process.clear()
                self.process.feed(text)
                if(self.num>500):
                    continue
                for k in range(2,self.page+1):
                    text=self.weiboCrawlPage(urlFollow.format(uid=uid,page=k))
                    self.process.clear()
                    self.process.feed(text)
                
                text=self.weiboCrawlPage(urlFans.format(uid=uid, page=1))
                self.process.clear()
                self.process.feed(text)
                if(self.num>500):
                    continue
                for k in range(2,self.page+1):
                    text=self.weiboCrawlPage(urlFans.format(uid=uid, page=1))
                    self.process.clear()
                    self.process.feed(text)
                
                self.userAdd(level)
                
                
                
            
        