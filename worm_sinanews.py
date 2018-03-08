import urllib.request
import re
url="http://news.sina.com.cn/"
data=urllib.request.urlopen(url).read().decode('utf-8','ignore')#打开网址并编码，Ignore参数选择性

pat='href="(http://news.sina.com.cn/.*?)"'
allurl=re.compile(pat).findall(data)
print(allurl)

for i in range(0,len(allurl)):
     thisurl=allurl[i]
     file="E:/Python教程/练习文件/新浪新闻/"
     file=file+str(i)+".html"
     urllib.request.urlretrieve(thisurl,file)