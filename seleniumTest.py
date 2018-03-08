from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re

browser=webdriver.Firefox()
url="http://wenshu.court.gov.cn/"
keyword="索普"
pat='href="(/content/content?DocID=.*?&KeyWord="'+keyword+')'
urllist=[]

browser.get(url)
elem1=browser.find_element_by_id("gover_search_key")
elem1.clear()
elem1.send_keys(keyword)
searchbutton=browser.find_element_by_class_name("head_search_btn")#中国裁判文书网找这个搜索按钮一定要用
searchbutton.click()
elem1=WebDriverWait(browser,10).until(
     EC.presence_of_element_located((By.ID,"pageNumber"))
)#设置等待时间
data=browser.page_source#page_source方法输出的字符串，一定要Encode编码转换成二进制才能open出来
browser.close()
fh=open('E:/Python教程/练习文件/中国裁判文书网/1.htm','wb')
fh.write(data.encode("utf-8"))
fh.close()
'''
print(pat)
re.compile(pat).findall(data)
print(urllist)'''
