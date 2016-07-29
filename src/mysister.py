#!/usr/bin/python
#coding=utf-8
import urllib2
import traceback
import os
import sys
import time
from BeautifulSoup import BeautifulSoup

homepage='http://www.lewenwu.com/books/31/31154/'
folder = "../atricle/"

def menu():	
	request = urllib2.Request("http://www.lewenwu.com/books/31/31154/")
	request.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36')
	doc = urllib2.urlopen(request)
	html = BeautifulSoup(doc)
	Domchapterlist=html.findAll("ul",{"class":"chapterlist"})
	chapterlist=Domchapterlist[0].findAll("a")
	i=1
	for a in chapterlist:
		print i,homepage+a['href'],a.text
		i=i+1
		page(homepage+a['href'],a.text)
		time.sleep(1)

def page(pageindex,title):	
	request = urllib2.Request(pageindex)
	request.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36')
	doc = urllib2.urlopen(request)
	html = BeautifulSoup(doc)
	context=html.findAll(id='content');
	text="\r\n=================================\r\n"+title+"\r\n=================================\r\n"
	text=text+context[0].text+''
	text=text.replace("&nbsp;","\r\n")
	text=text.replace("go","")
	text=text.replace("over","")

	fp=open("text"+".txt","a")
	fp.write(text)
	fp.close()

if __name__ == '__main__':
	reload(sys)
	sys.setdefaultencoding('utf-8') 
	print "START"

	menu()
	
	# page("http://www.lewenwu.com/books/31/31154/10792732.html","第一百零九章 异子而换")

	print "END"
