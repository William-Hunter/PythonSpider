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
		page(homepage+a['href'],a.text)
		i=i+1	
		time.sleep(1)

def page(pageindex,title):	
	request = urllib2.Request(pageindex)
	request.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36')
	
	doc = access(request)
	html = BeautifulSoup(doc)
	content=html.findAll(id='content');	
	while not content:
		doc = access(request)
		html = BeautifulSoup(doc)
		content=html.findAll(id='content');

	text="\r\n\r\n=================================\r\n"+title+"\r\n=================================\r\n"
	text=text+content[0].text+''
	text=text.replace("&nbsp;","\r\n")
	text=text.replace("go","")
	text=text.replace("over","")

	fp=open("text"+".txt","a")
	fp.write(text)
	fp.close()

def access(request):
	return urllib2.urlopen(request)

if __name__ == '__main__':
	reload(sys)
	sys.setdefaultencoding('utf-8') 
	print "START"

	menu()
	
	# page("http://www.lewenwu.com/books/31/31154/6613420.html","楔子")

	print "END"
