# import requests
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'zh-CN,zh;q=0.9',
#   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
# }
# t=requests.get('https://sh.lianjia.com/zufang/SH2302863702782640128.html',headers=DEFAULT_REQUEST_HEADERS)
#
# print(t.text)
# import re
# s='整租·广海花园 3室1厅 南'
# # s='整租·翠苑(公寓) 2室1厅 南'
# r=re.findall('·(.*?)\s',s)[0]
# # r=re.findall(s,r'·(\w)\s')
# print(r)
# s='1\n20\n98562\n'
# print(s.replace('\n',' '))
# import datetime
# print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

def get_start_urls():
  base_url = 'https://sh.lianjia.com/zufang'
  # 按租金划分 /brp3000erp9000/
  for i in range(3000, 25000, 500):
    print(i, i + 500)
get_start_urls()


