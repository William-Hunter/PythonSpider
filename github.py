#coding=utf-8
import urllib2
from BeautifulSoup import BeautifulSoup
homepage='https://github.com'
def work(homepage,key):
	doc = urllib2.urlopen(homepage)
	html = BeautifulSoup(doc)
	filelistlink=html.findAll('a','js-navigation-open')
	if(filelistlink):
		print "TRUETRUETRUETRUETRUETRUETRUETRUETRUETRUETRUETRUETRUE"
		for row in filelistlink:
			print '-------------------------------------------------------------------------------------------------------------'
			print row		
	else:
		print "FALSEFALSEFALSEFALSEFALSEFALSEFALSEFALSEFALSEFALSE"

if __name__ == '__main__':
	work('https://github.com/Titzanyic/RiddleAndroidProject','')
	print "END"