#!/usr/bin/python
#coding=utf-8
import urllib2
import traceback
import os
import sys
import requests
from BeautifulSoup import BeautifulSoup

homepage='http://www.u6f4.com'
folder = "../pornimg/"
keyword='aaaa'

def menu():	
	request = urllib2.Request("http://www.u6f4.com/AAtupian/AAtb/")
	request.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36')
	doc = urllib2.urlopen(request)
	html = BeautifulSoup(doc)
	category=html.findAll("li",{"class":"menu-item"})
	index=0
	menu=[]
	for zoo in category:
		menu.append(homepage+zoo.a['href'])
		print index,":",zoo.a.text
		index=index+1
	menuindex=menu[input("请输入进入哪个菜单:")]
	keyword=raw_input("输入你想要的关键字:")
	page(menuindex,keyword)
	
def page(pagePath,keyword):
	request = urllib2.Request(pagePath)
	request.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36')
	doc = urllib2.urlopen(request)
	html = BeautifulSoup(doc)
	viewlist=html.findAll("div",{"class":"box list channel"})
	
	viewlinks=viewlist[0].findAll("a")
	for viewlink in viewlinks:
		if keyword in viewlink.text:
			print viewlink.text,"page"
			view(homepage+viewlink['href'],viewlink.text)

	nextpagelist = html.findAll("a", {"class" : "pagegbk"})
	for next in nextpagelist:
		if "下一页" in next.text:
			nextpage=homepage+next['href']
			print 'nextpage-------',nextpage
			page(nextpage,keyword)

def view(viewpath,title):
	if not os.path.exists(folder+title):
		os.makedirs(folder+title)

	request = urllib2.Request(viewpath)
	request.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36')
	doc = urllib2.urlopen(request)
	html = BeautifulSoup(doc)
	viewlist=html.findAll("img")
	for img in viewlist:
		download(img['src'],title)

def download(src,title):
	srctrim=src.split("/")
	srctrim=srctrim[len(srctrim)-1]

	imgname=srctrim+".jpg"
	path = folder+title+"/"+imgname
	request = urllib2.Request(src)
	request.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36')
	conn = urllib2.urlopen(request)
	f = open(path,'w')  
	f.write(conn.read())  
	f.close()  
	print(imgname+'\t\tSaved!')


if __name__ == '__main__':
	reload(sys)
	sys.setdefaultencoding('utf-8') 
	print "START"

	# view("http://www.u6f4.com/AAtupian/AAwz/e225845aff406b21ce8ab3a0860be756.html","yaotou")
	
	function={ '1':menu	}
	function.get(raw_input("1:ccc26Porn image\ninput:"))()

	print "END"
