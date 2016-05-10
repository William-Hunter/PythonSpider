import urllib2
from BeautifulSoup import BeautifulSoup

print "start"

doc = urllib2.urlopen("http://bbs.dvd9000.com/html/0~200.html")
html = BeautifulSoup(doc)

menu=html.findAll('div',id='postnavi')
print menu
# BeautifulSoup(menu)
# print menu.findAll("a")


