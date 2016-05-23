#!/usr/bin/env python3  
#coding: utf-8  
import smtplib  
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  
from email.mime.image import MIMEImage
servername = 'smtp.126.com'    
# username = raw_input("input username:")
username = "iwantfunkyou@126.com"
# password=raw_input("input password:")
password="fuckfuckfuck"
# receiver = raw_input("input receiver:")
receiver = "1344014631@qq.com"
msgRoot = MIMEMultipart('related')  
msgRoot['Subject'] = "shit"
#构造附件 
att = MIMEText(open("target/0~200.txt", 'rb').read(), 'base64', 'utf-8')  
att["Content-Type"] = 'application/octet-stream'  
att["Content-Disposition"] = 'attachment; filename="0~200.txt"'  
msgRoot.attach(att)  
smtp = smtplib.SMTP()   
smtp.connect(servername, "25")   
smtp.login(username, password)   
smtp.sendmail(username, receiver, msgRoot.as_string())   
smtp.quit()  
print "done"