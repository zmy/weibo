#coding=utf-8

import urllib.request as http#instead of urllib2
import urllib.parse #urlencode is used
import http.cookiejar as cookie
import re
import sys


class WeiboLogin:
    def __init__(self,username,password):
        self.infodata={}
        self.pwd=password
        self.infodata['remember']='on'
        self.infodata['backURL']='http%3A%2F%2Fweibo.cn%2F'
        self.infodata['submit']='%B5%C7%C2%BC'
        self.infodata['mobile']=username
        self.infodata['backTitle']='%CA%D6%BB%FA%D0%C2%C0%CB%CD%F8'
        self.loginPage='http://3g.sina.com.cn/prog/wapsite/sso/'
    def getAttribute(self):
        url='http://3g.sina.com.cn/prog/wapsite/sso/login.php?backURL=http%3A%2F%2Fweibo.cn%2F&backTitle=%D0%C2%C0%CB%CE%A2%B2%A9&vt=4&revalid=2&ns=1'
        text=urllib.request.urlopen(url).read()
        text=text.decode('UTF-8')
        #print(text)
        p=re.compile(r'<form action="(.*) m')
        value=p.search(text).group(1)
        print(value)
        self.loginPage+=value
        p=re.compile(r'<input type="password" name="(.*)" s')
        value=p.search(text).group(1)
        self.infodata[value]=self.pwd
        print(value)
        p=re.compile(r'''<input type="hidden" name="vk" value="(.*)"''')
        value=p.search(text).group(1)
        self.infodata["vk"]=value
        print(value)
    def login(self):
        self.getAttribute()
        try:
            cj=cookie.CookieJar()
            self.opener=http.build_opener(http.HTTPCookieProcessor(cj))
            self.opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0')];
            print(self.infodata)
            data= urllib.parse.urlencode(self.infodata)
            data= data.encode(encoding='UTF8')
            rsp = self.opener.open(self.loginPage,data)
            homePage = rsp.read().decode('UTF-8','ignore')
            p=re.compile(r'Fgsid%(.*)+%')
            return p.search(homePage).group(1)
        except Exception as e:
            print(e)
            print("fail to log in")
            return None
    def crawlPage(self,url):
        text=self.opener.open(url)
        value=text.read().decode('UTF-8')
        value=value.replace("&#039;","'")
        value=value.replace("&nbsp;"," ")
        return value
if __name__=="__main__":
    s=WeiboLogin('chengyong3001@gmail.com','mydream2012')
    #print("!!!!")
    text='''<form action="login_submit.php?rand=896793020&amp;backURL=http%3A%2F%2Fweibo.cn%2F&amp;backTitle=%D0%C2%C0%CB%CE%A2%B2%A9&amp;vt=4&amp;revalid=2&amp;ns=1" method="post">
<div class="mg">'''
    p=re.compile(r'''<form action=(.*)''')
    value=p.search(text).group(1)

    print(value)
    #s.getAttribute()
    s.login()
    
    text=s.crawlPage("http://weibo.cn/1036663592/follow?page=1&vt=4&gsid=3_5bcf0c5bea3f4fc4ffb4d7ce3c47e6a6f54a265b88c8")
    sys.stdout=open('res.out','w')
    print(text)   
            
            
            
            
            
            