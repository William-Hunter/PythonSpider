import urllib2
import traceback
import os
import sys
from BeautifulSoup import BeautifulSoup
reload(sys)
sys.setdefaultencoding( "utf-8" )

ranger={'0~200','200~400','400~600','600~800','800~1000','1000~1200','1200~1400','1400~1600','1600~1800','1800~2000','2000~2200','2200~2400','2400~2600','2600~2800','2800~3000','3000~3100'}
os.remove("target/*.txt")
# for ran in ranger:
# 	fp=open("target/"+ran+".txt","w")
# 	url="http://bbs.dvd9000.com/html/"+ran+".html"
# 	fp.write(url+"\n\n")
# 	doc = urllib2.urlopen(url)
# 	print "\n-------------",url
# 	html = BeautifulSoup(doc)
# 	tdlist=html.findAll('td',align='left')
# 	i=1
# 	for td in tdlist:
# 		print i
# 		i+=1
# 		try:
# 			subtitle=td.contents[2]
# 		except TypeError, e:
# 			subtitle=''
# 		try:
# 			link=td.a['href']	
# 		except TypeError, e:
# 			link=''
# 		fp.write(subtitle+"\n")
# 		fp.write(link+"\n\n")
# 	fp.close()
			