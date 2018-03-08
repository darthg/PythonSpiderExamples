import  xlsxwriter

def create_xls(path):
     try:
          wb=xlsxwriter.Workbook(path)
          return wb
     except Exception as e:
        print("创建表格出错："+str(e))



filepath=r'E:/Python教程/练习文件/豆瓣出版商.xls'
fl=create_xls(filepath)
fl.close()
