# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 11:52:20 2018

@author: nishil
"""

import jobapp
#%% Main
what, where = 'Statistics','Arlington, VA'
num_pages = 3

url = jobapp.IndeedSearch(what, where)
joblist = jobapp.Indeedjoblistpage(url)
urllist = joblist.geturls(num_pages)

unwanted = ['US citizen', "TS", "SCI", "DoD", "TOP SECRET", "Top secret"]
urlresult = jobapp.CheckWordsIn(unwanted,urllist)

#%%
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#%%
sender = "sender_email@gmail.com"
receiver = "receiver_email@gmail.com"
password = "sender_password"

msg = MIMEMultipart()
msg["From"] = sender
msg["To"] = receiver
msg["Subject"] = "Indeed - " + what + " in "+ where

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
#Next, log in to the server
server.login(sender, password)
unwanted_words = ", ".join(unwanted)
urls = "\n".join(urlresult)
body = "Jobs below have has no following words: " + unwanted_words + "\n" + urls
msg.attach(MIMEText(body))
server.sendmail(sender,receiver,msg.as_string())
server.quit()
