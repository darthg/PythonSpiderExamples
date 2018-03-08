import urllib.request

def use_proxy(url,ip):
     proxy=urllib.request.ProxyHandler({"http":ip})#设立代理IP
     opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)#封装opener
     urllib.request.install_opener(opener)#将opener设立成全局变量
     data=urllib.request.urlopen(url).read().decode("utf-8","ignore")#爬取网页内容
     return  data



proxy_ip="111.155.116.216:8123"
url="http://www.baidu.com"
data=use_proxy(url,proxy_ip)
print(len(data))