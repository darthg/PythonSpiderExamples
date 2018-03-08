import xlsxwriter
import xlwt
import  re
import  urllib.request

pattern='<div class="name">(.*?)</div>'
url='https://read.douban.com/provider/all'
code='UTF-8'


def getpubliclist(pat,url,decode):
     data=urllib.request.urlopen(url).read().decode(decode)
     rst=re.compile(pat).findall(str(data))
     return rst

def create_xls(path):
     try:
          wb=xlsxwriter.Workbook(path,)
          return wb
     except Exception as e:
        print("创建表格出错："+str(e))


result=getpubliclist(pattern,url,code)
#print(result)
print('出版商数量共计：'+str(len(result)))



filepath=r'E:/Python教程/练习文件/豆瓣出版商.xls'
fl=create_xls(filepath)
fp=[]
fp=[fl.add_worksheet('豆瓣出版商')]
print(fp)
fp.append(fl.add_worksheet("2"))
print(fp[0])
fl.close()



'''for i in range(len(result)):
     print('正在写入出版商：'+str(i)+str(result[i])+'\n')
     fp.write(i,0,result[i])
fl.close()'''


