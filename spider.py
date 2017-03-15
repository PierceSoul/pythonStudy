# -*- coding: UTF-8 -*-
__author__ = 'Administrator'
import re
import urllib.parse
import urllib.request as request
import os,uuid
from multiprocessing import Pool
from multiprocessing import Process, freeze_support
import multiprocessing
localPath='/Users/Tong/Documents/testttt'
#res = r'top'
#str = "top iip"
#print(re.findall(res,str))
#def getHtml(url):
#    page = urllib.request.urlopen(url)
#    html = page.read().decode('htf-8')
#    return html
#print(getHtml("http://jandan.net/ooxx/page-2008# #comments"))
url = "http://tieba.baidu.com/p/4784749512?see_lz=1"
req = request.Request(url, headers = {
    "Connection": "Keep-Alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "h-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0"
})
data = request.urlopen(req).read()

def getImg(html):
    reg = r'(http://imgsrc.baidu.com/forum/w%3D580[^\s]*?(jpg))'
    imgUrl = re.compile(reg)
    imgList =  re.findall(imgUrl,html)
    listre = []
    for i in imgList:
        listre.append(i[0])
    return listre


#根据文件名创建文件
def createFileWithFileName(localPathParam,fileName):
    totalPath=localPathParam+'/'+fileName
    if not os.path.exists(totalPath):
        file=open(totalPath,'a+')
        file.close()
        return totalPath

#生成一个文件名字符串
def generateFileName():
    return str(uuid.uuid1())[0:7]


def getAndSaveImg(imgUrl):
    if( len(imgUrl) != 0 ):
        fileName=generateFileName()+'.jpg'
        request.urlretrieve(imgUrl,createFileWithFileName(localPath,fileName))

imgList = getImg(data.decode())
#def saveImg(list):
#    for url in list:
#        getAndSaveImg(url)
#        print(url)
#saveImg(imgList)
print(imgList)
if __name__ == "__main__":
   multiprocessing.freeze_support()
   cpu_number = multiprocessing.cpu_count()
   pool = Pool()
   pool.map(getAndSaveImg, imgList)


#print("done")