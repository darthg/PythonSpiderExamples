import urllib.request
import re

keyname=urllib.request.quote("童装")#给搜索关键词编码
allurl_pic=[]
headers=('User-Agent',"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36")
opener=urllib.request.build_opener()
opener.addheaders=[headers]#浏览器伪装，封装报文头部

for i in  range(0,3):
     url='https://s.taobao.com/search?q='+keyname+'&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=4&ntoffset=4&p4ppushleft=1%2C48&s='+str(i*44)
     data=opener.open(url).read().decode("utf-8","ignore")
     pat='"pic_url":"(.*?)"'
     allurl_pic.append(re.compile(pat).findall(data))
print(len(allurl_pic))

#开始下载图片
for i in range(0,len(allurl_pic)):
     for j in  range(0,len(allurl_pic[i])):
          allurl_pic[i][j]="http:"+allurl_pic[i][j]
          filepath='E:/Python教程/练习文件/淘宝童装图片/'+keyname+'_'+str(i)+'_'+str(j)+'.jpg'
          urllib.request.urlretrieve(allurl_pic[i][j],filepath)#urlretrieve方法中的filepath要精确到文件名，文件夹是不行的
          print("已下载第"+str(i)+"页的第"+str(j)+"张图片...")

