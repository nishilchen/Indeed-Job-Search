# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 21:26:35 2018

@author: nishil
"""
#%% Import Packages
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
#%%
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#%%
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
   
# =============================================================================
#     def CheckWordIn(self,word,tag):
#         soup = self.getsoup()
#         return [a for a in soup.findAll(tag) if word in repr(a)]
# =============================================================================
    
    
#%% Indeed Specific

class Indeedjoblistpage(jobpage):
    src = 'https://www.indeed.com'
    def findjobmap(self):
        soup = self.getsoup()
        return [a for a in soup.findAll('a') if 'jobmap' in repr(a)]
    
    
    def geturl(self):
        jobmap = self.findjobmap()
        #jobmap = self.CheckWordIn('jobmap')
        result = []
        for j in jobmap:
            if '/rc/clk?' in j['href']:
                result.append(self.src + '/viewjob' + j['href'][7:])
            else:
                result.append(self.src + j['href'])
        return result

    def IndeedNextPage(self,url):
        if '&start' in self.url:
            strings = self.url.split('&start=')
            page = '&start=' + str(int(strings.pop()) + 10)
            self.url = strings[0] + page
            return self.url
        else:
            self.url = self.url + '&start=10'
            return self.url

    def geturls(self,pages):
        results = []
        for i in range(pages):
            results.extend(self.geturl())
            self.url = self.IndeedNextPage(self.url)
        return results
#%%
def IndeedSearch(what, where):
    src = 'https://www.indeed.com'
    return src + '/' + 'jobs?q=' + '+'.join(what.split(' ')) + '&l=' + '%2C+'.join(where.split(', '))
#%%
# =============================================================================
# for u in urllist:
#     try:
#         job = jobpage(u)
#         job.getsoup()
#         if 'US citizen' in repr(job.soup):
#             urllist.remove(u)
#     except:
#         print(u)
# =============================================================================
def CheckWordsIn(strings,urllist):
    urlresult = []
    for u in urllist:
        try:
            job = jobpage(u)
            job.getsoup()
            if any([s in repr(job.soup) for s in strings]):
                continue
            else:
                urlresult.append(u)
        except:
            pass
    return urlresult
#%% Main
what, where = 'Statistics','Arlington, VA'
num_pages = 3

url = IndeedSearch(what, where)
joblist = Indeedjoblistpage(url)
urllist = joblist.geturls(num_pages)
len(urllist)

unwanted = ['US citizen', "TS", "SCI", "DoD", "TOP SECRET", "Top secret"]
urlresult = CheckWordsIn(unwanted,urllist)
urlresult
len(urlresult)