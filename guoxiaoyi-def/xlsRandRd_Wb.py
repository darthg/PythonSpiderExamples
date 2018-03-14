import xlrd
import random
import xlsxwriter

def getPoxiesRand(filepath):
     try:
     #workbook=xlrd.open_workbook(r"E:\GitHub\测试文件\2016年保险明细报表.xls")
          workbook=xlrd.open_workbook(filepath)
     except Exception as e:
          print("读取代理IP池出现异常！请确认文件路径！")
     sheets=workbook.sheet_by_index(0)
     print("代理IP共有"+str(sheets.nrows)+'个')
     rand_no=random.randint(1,sheets.nrows-1)#注意边际范围
     IPAdrr=sheets.cell(rand_no,0).value
     #print(data)
     return IPAdrr#返回IP


#data=['122.114.31.177:808','61.135.217.7：80','120.92.88.202:10000']测试数据
def writeIPaddr(data):
     try:
          workbook = xlsxwriter.Workbook(r"E:\GitHub\测试文件\IP_pool.xls")
     except Exception as e:
          print("写入代理IP错误！")
     sheet=workbook.add_worksheet()
     sheet.write(0,0,'IP地址')
     sheet.write(0,1,'端口号')
     sheet.write(0,2,'匿名属性')
     sheet.write(0,3,'协议类型')
     sheet.write(0,4,'有效期')
     sheet.write(0,5,'验证时间')
     for i in range(1,len(data)+1):
          sheet.write(i,0,data[i-1])
     workbook.close()


#测试函数
#ip=getPoxiesRand(r"E:\GitHub\测试文件\IP_pool.xls")
#print(ip)