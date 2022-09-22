import requests
from time import sleep
from lxml import etree

baseURL = "https://tieba.baidu.com/f?"
headers = headres = {
'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'}


f = open(r'icookies.txt')
cookies = {}
for i in f.read().split(';'):
        name,value = i.strip().split('=',1)
        cookies[name] = value
print(cookies)

req = requests.get(baseURL,params={'kw':'赛博朋克2077'},cookies=cookies)
req.encoding = 'utf-8'
html = req.text
# print(html)
parseHtml = etree.HTML(html)
userID = parseHtml.xpath('//*[@id="j_u_username"]/div/a/span/text()')
v = parseHtml.xpath('//*[@id="thread_top_list"]/li/div/div[2]/div/div[1]/a/text()')
v1 = parseHtml.xpath('//*[@id="thread_list"]/li/div/div[2]/div[1]/div[1]/a/@href')
print(userID)
print(v)
print(v1)
print(req.url)

