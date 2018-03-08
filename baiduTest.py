import urllib.request
import urllib.parse

url='http://www.iqianyue.com/mypost/'
logindata=urllib.parse.urlencode({'name':'usstxiaoyi'},{'pass':'coldfalling525'}).encode('utf-8')
req=urllib.request.Request(url,logindata)
#req.add_header()
urldata=urllib.request.urlopen(req).read()

fh=open(r'E:\Python教程\练习文件\2.html','wb')
fh.write(urldata)
fh.close()
