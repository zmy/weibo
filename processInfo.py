#coding=utf-8
from html.parser import HTMLParser
import re
class ProcessInfo(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.clear()
        self.init()
    def clear(self):
        self.infoBase=False
        self.infoSchool=False
        self.isDiv=False
        self.isA=False
        self.num=0
        self.page=0
        self.caculateNum=False
        self.isSpan=False
        self.isTable=False
        self.isTd=False
        self.aValue=""
        self.isTag=False
    def init(self):
        self.info=[]
        self.tag=[]
        self.school=[]
        self.array=[]
    def setIsTag(self):
        self.isTag=True
    def handle_starttag(self,tag,attrs):
        if(tag=='div'):
           # print("****")
            self.isDiv=True
            for key,value in attrs:
                if(key=='class' and value=='tip'):
                    self.infoBase=False
                    self.infoSchool=False
                elif(key=='class' and value=='tip2'):
                    self.caculateNum=True       
        elif(tag=='td'):
            for key,value in attrs:
                if(key=='style' and value=='width: 52px'):
                    self.isTd=True
        elif(tag=='a'):
            self.isA=True
            if(self.isTag):
                self.isA=False
            for key,value in attrs:
                if(key=='href'):
                    self.aValue=value
                    if(value.startswith('/search')):
                        self.isA=True       
        elif(tag=='input'):
            flag=False
            for key,value in attrs:
                if(key=='name' and value=='mp'):
                    flag=True
                elif(key=='value' and flag):
                    self.page=int(value)
        elif(tag=='span'):
            for key,value in attrs:
                if(key=='class' and value=='tc'):
                    self.isSpan=True
    def handle_endtag(self,tag):
        if(tag=='div'):
            self.isDiv=False
        elif(tag=='td'):
            self.isTd=False
        elif(tag=='a'):
            self.isA=False
    def handle_data(self,data):
        if(self.isDiv==True):
            if(data=='����Ϣ'):
                self.infoBase=True
            elif(data=='ѧϰ����'):
                self.infoSchool=True
            elif(self.infoBase):
                if(data=='��ǩ:'):
                    self.infoBase=False
                else:
                    self.info.append(data)
            elif(self.infoSchool):
                self.school.append(data)
            elif(self.isSpan):
                p=re.compile(r'\d+')
                #print(data)
                self.isSpan=False
                #print(p.search(data).group())
                self.num=int(p.search(data).group())
        if(self.isA):
            if(self.isTag):
                self.tag.append(data)
            elif(data.startswith('��ע')):
                p=re.compile(r'uid=(\d+)&')
                self.array.append(p.search(self.aValue).group(1))
if __name__=="__main__":
    name='����'
    #text=open('res.out','r').readlines()
    fp=open('res.out','r')
    text=fp.read()
    print(text)
   # text='''<div class="tip">����Ϣ</div><div class="c">�ǳ�:zmoony<br/>����:���� ��ʳ ��Ϸ <br/>�Ա�:��<br/>����:���� ������<br/>����:˫����<br/>��ȡ��Ů<br/>����״��������<br/>���:Though I&#039;m not always the best, I&#039;ll always try my best.<br/>��ǩ:<a href="/search/?keyword=maTHmU&amp;stag=1&amp;vt=4&amp;gsid=3_5bcf0c5bea3f4fc4ffb4d7ce3c47e6a6f54a265b88c8">maTHmU</a>&nbsp;<a href="/search/?keyword=%E8%B4%B5%E9%99%A2&amp;stag=1&amp;vt=4&amp;gsid=3_5bcf0c5bea3f4fc4ffb4d7ce3c47e6a6f54a265b88c8">��Ժ</a>&nbsp;<a href="/search/?keyword=%E6%B8%85%E5%8D%8E%E5%A4%A7%E5%AD%A6&amp;stag=1&amp;vt=4&amp;gsid=3_5bcf0c5bea3f4fc4ffb4d7ce3c47e6a6f54a265b88c8">�廪��ѧ</a>&nbsp;<a href="/account/privacy/tags/?uid=1748153860&amp;vt=4&amp;gsid=3_5bcf0c5bea3f4fc4ffb4d7ce3c47e6a6f54a265b88c8">���&gt;&gt;</a><br/>'''
    s=ProcessInfo()
    s.feed(text)
    print(s.info)
    print(s.school)   
    print(s.page)
    print(s.array)
    print(s.num)        
                
                
            
            
