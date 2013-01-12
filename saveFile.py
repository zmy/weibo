#coding=utf-8
class FileSave:
    def __init__(self,path):
        self.profile=open(path+'profile.out','w')
        self.follow=open(path+'follow.out','w')
        self.fan=open(path+'fan.out','w')
    def addProfile(self,uid,str):
        self.profile.write(str)
        self.profile.flush()
    def addFollow(self,uid,str):
        self.follow.write(str)
        self.profile.flush()
    def addFan(self,uid,str):
        self.fan.write(str)
        self.fan.flush()
    def save(self):
        self.fan.close()
        self.profile.close()
        self.follow.closer()
    def __del__(self):
        self.save()
        
        
    
