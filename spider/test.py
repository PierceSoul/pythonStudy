
import requests
import codecs
from multiprocessing import Pool
import os

file_dic = "车镇易购"
if not os.path.isdir(file_dic):
    os.makedirs(file_dic)

url = u"http://www.chezhency.com/home/shop_info/perinfo/ucid/"

def spider(user_ID):
    request_url = url + str(user_ID) + '.html'
    print("正在下载 " + request_url)
    response = requests.get(request_url)
    if response.ok:
        file = codecs.open(file_dic + '/' + str(user_ID) + '.html', mode='w+', encoding='utf-8')
        file.write(str(response.content, encoding='utf-8'))
        file.close()

#pool = Pool()
my_list = list(range(1, 20))
#pool.map(spider, my_list)
# 最大ID是8086
for id in my_list:
    spider(id)
print("done")