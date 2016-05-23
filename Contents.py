import urllib2
from BeautifulSoup import BeautifulSoup
homepage='http://tt.71wx.net/xiaoshuo/5/5704/'
doc = urllib2.urlopen(homepage)
html = BeautifulSoup(doc)
menu=html.findAll('div','centent')
contents=menu[0].findAll('a')
for e in contents:
	print '------'
	print e.string
	# fp=open("airticle/"+e.string+".txt","w")	
	print homepage+e['href']
	chapters=urllib2.urlopen(homepage+e['href'])
	chapters = BeautifulSoup(chapters)
	print chapters



