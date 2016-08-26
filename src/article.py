#! /usr/bin/env python
#-*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
import urllib2
import traceback
import os
import sys
import requests
homepage=''
bookname=''
pageattr=''
pageattrvalue=''
def createFile(bookname):	
	if not os.path.isdir("../article"):
		os.mkdir('../article')	
	if not os.path.isfile('../article/'+bookname+'.txt'):
		os.mknod('../article/'+bookname+'.txt')
	return 1
def access(url):
	request = urllib2.Request(url)
	request.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36')
	return urllib2.urlopen(request)
def menu(menuurl,attr,style):	
	doc=access(menuurl)
	while not doc:
		doc=access(menuurl)
	html = BeautifulSoup(doc)	
	lilist=html.findAll('ul',{attr:style})
	alist=lilist[0].findAll('a')
	for a in alist:
		if a['href'].startswith('/') or a['href'].startswith('\\'):
			page(homepage+a['href'],a.text)
		else:
			page(menuurl+'/'+a['href'],a.text)
def page(pageurl,title):	
	print pageurl,title
	doc=access(pageurl)
	html = BeautifulSoup(doc)
	content=html.findAll('div',{pageattr:pageattrvalue})
	while not content:
		doc=access(pageurl)
		html = BeautifulSoup(doc)
		content=html.findAll('div',{pageattr:pageattrvalue})
	# optimize content
	text='\n\n\n==============================\n'+title+'\n==============================\n'
	text=text+content[0].text.replace('&nbsp;&nbsp;&nbsp;&nbsp;','\n')
	text=text.replace('go','')
	text=text.replace('over','')
	text=text.replace('reads();','')
	# optimize over
	write(text)
def	write(text):
	fp=open('../article/'+bookname+'.txt','a')
	fp.write(text)
	fp.close()
if __name__=='__main__':
	reload(sys)
	sys.setdefaultencoding('utf-8')
	print "START"	
	# bookname=raw_input('input book name:')
	# homepage=raw_input('input the home path:')
	# #homepage without '/'	
	# menuurl=raw_input('input your menu url:')
	# attr=raw_input('input the attr:')
	# style=raw_input('input the ul style:')
	# pageattr=raw_input('input page attr:')
	# pageattrvalue=raw_input('input page style:')
	bookname='京门风月'
	homepage='http://www.lewenwu.com'
	menuurl='http://www.lewenwu.com/books/31/31154'
	attr='class'
	style='chapterlist'
	pageattr='id'
	pageattrvalue='content'
	if createFile(bookname):
		menu(menuurl,attr,style)
	print "END"