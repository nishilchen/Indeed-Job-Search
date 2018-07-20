# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 21:26:35 2018

@author: nishi
"""
#%%
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

class jobpage:
    def __init__(self, url):
        self.url = url
        self.html = None
        self.soup = None
        
    def gethtml(self):
        self.html = urllib.request.urlopen(self.url, context = ctx).read()
        return self.html
    
    
    def getsoup(self):
        html = self.gethtml()
        self.soup = BeautifulSoup(html, "html.parser")
        return self.soup
   
    def CheckWordIn(self,word,tag):
        soup = self.getsoup()
        return [a for a in soup.findAll(tag) if word in repr(a)]
    
    
#%% Indeed Specific
class Indeedjoblistpage(jobpage):
    def findjobmap(self):
        soup = self.getsoup()
        return [a for a in soup.findAll('a') if 'jobmap' in repr(a)]
    
    
    def geturl(self):
        jobmap = self.findjobmap()
        #jobmap = self.CheckWordIn('jobmap')
        src = 'https://www.indeed.com'
        result = []
        for j in jobmap:
            if '/rc/clk?' in j['href']:
                result.append(src + '/viewjob' + j['href'][7:])
            else:
                result.append(src + j['href'])
        return result




#%%
url = 'https://www.indeed.com/jobs?q=data+scientist&l=Washington%2C+DC'
joblist = Indeedjoblistpage(url)
urllist = joblist.geturl()

for u in urllist:
    try:
        job = jobpage(u)
        job.getsoup()
        if 'US citizen' in repr(job.soup):
            urllist.remove(u)
    except:
        print(u)
    






#%%
# =============================================================================
# def gethtml(url):
#     html = urllib.request.urlopen(url, context = ctx).read()
#     return html
# 
# 
# def getsoup(html):
#     soup = BeautifulSoup(html, "html.parser")
#     return soup
# =============================================================================

#%%
        
        
        
        
        
#def CheckWordIn:
#def CheckWordNotIn:
        
        
        
        