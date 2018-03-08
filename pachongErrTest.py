'''import urllib.error
import urllib.request

try:
     urllib.request.urlopen("http://blog.csdn.net")
except urllib.error.HTTPError as e:
     if hasattr(e,"code"):
          print(e.code)
     if hasattr(e,"reason"):
          print(e.reason)'''

import  urllib.request

url='http://blog.csdn.net/darthg'
headers=("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
data=opener.open(url).read()
fh=open(r'E:\Python教程\练习文件\3.html','wb')
fh.write(data)
fh.close()
