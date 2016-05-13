#!/usr/bin/env python3  
#coding: utf-8  
import smtplib  
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  
from email.mime.image import MIMEImage  
  
username = 'willliam113758@126.com'  
password = 'lonedon'
sender = username  
receiver = 'a709209619@qq.com'  
subject = 'python email test'  
servername = 'smtp.exmail.126.com'  
  
  	
msgRoot = MIMEMultipart('related')  
msgRoot['Subject'] = 'test message'  
  
#构造附件  
att = MIMEText(open('target/0~200.txt', 'rb').read(), 'base64', 'utf-8')  
att["Content-Type"] = 'application/octet-stream'  
att["Content-Disposition"] = 'attachment; filename="0~200.txt"'  
msgRoot.attach(att)  

smtp = smtplib.SMTP()
print 1
smtp.connect(servername)  
print 2
print "login"+smtp.login(username, password)  
print "send"+smtp.sendmail(sender, receiver, msgRoot.as_string())  
smtp.quit() 