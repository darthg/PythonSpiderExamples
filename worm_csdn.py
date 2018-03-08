import urllib.request
import re

url="http://blog.csdn.net/"
headers=('User-Agent',"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
data=opener.open(url).read().decode('utf-8','ignore')
pat='href="(http://blog.csdn.net/.*?/article/.*?)"'
pat2='href="http://blog.csdn.net/.*?/article/.*?" target="_blank">(.*?)</a>'
allurl=re.compile(pat).findall(data)


for i in range(0,len(allurl)):
     try:
          thisurl=allurl[i]
          file="E:/Python教程/练习文件/csdn文章列表/"
          file=file+str(i+1)+".html"
          urllib.request.urlretrieve(thisurl,file)
          print("正在爬取第"+str(i+1)+"篇文章...")
     except Exception as e:
          print(e)
          continue