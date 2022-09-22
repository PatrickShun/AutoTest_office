import urllib.request
import urllib.parse
from lxml import etree
import xlrd
import xlwt
import time

class JiraBugList():
    """docstring for JiraBugList"""
    def __init__(self):
        # self.bugKey = input('请输入Bug号：\n')
        self.baseURL = 'http://jira.vw-mobvoi.com:8080/browse/'
        self.headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        #Accept-Encoding: gzip, deflate
        "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
        "Connection":"keep-alive",
        # "Cookie":"seraph.rememberme.cookie=23407%3A14385c74aadd45f98fb09fd90ea87afa264be13c; JSESSIONID=B846833F4D2C8A1CD3B1BF1E69C9475F; atlassian.xsrf.token=B6VW-6ZIG-SH3J-D7SH_9a463a8cab42e4461a9da1534fd22b029b67da6b_lin; jira.editor.user.mode=wysiwyg",
        "Cookie":"jira.editor.user.mode=wysiwyg; JSESSIONID=8650FA95B5D0B39A8608E738DDA29EB7; seraph.rememberme.cookie=27714:ed7d8c779be4e63cfe4d2c8cc0df1896a0737bc3; atlassian.xsrf.token=B6VW-6ZIG-SH3J-D7SH_3216ffa54b3d84d2c58dc4bae41de94bcdc81676_lin",
        "Host":"jira.vw-mobvoi.com:8080",
        "Referer":"http://jira.vw-mobvoi.com:8080/issues/?filter=-2",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        }


        # 需要增加人名    
        self.VWM_list = ['xingqi ye','xiaoyan chen','jinghui wang','bo wang','xiongshun lan','zhanfei li','ying yan','shunfu tian','huishuang xue','mingzhen huang','yang wang','jinlei cao','jiaqi liu','xiujiao zhao','zhe li','kaifan guo',]
        self.Mobvoi_list = ['jingyi.jia@mobvoi.com','qingtao.li@mobvoi.com','guanghui wei','linxu.xia','han zhang','liming.wang@mobvoi.com','chenchen.zeng@mobvoi.com','yue.liao@mobvoi.com','liming.wang@mobvoi.com','jiabin niu','yuliang yuliang ','fllin']

        self.status = []
        self.tittle = []
        self.lever = []
        self.cause = []
        self.assignee = []
        self.Responsible_party = []
        self.createtime = []



    def readExcel(self):
        try:
            data = xlrd.open_workbook('1.xls')
            table = data.sheets()[0]
            tableValueCol = table.col_values(0)
            return tableValueCol
        except Exception:
            print(e)


    def getPage(self,url):
        time.sleep(0.5)
        req = urllib.request.Request(url,headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode('utf-8')
        self.parsePage(html)


    def parsePage(self,html):
        parseHtml = etree.HTML(html)
        tittle = parseHtml.xpath("//h1[@id='summary-val']/text()")[0].strip()
        lever = parseHtml.xpath("//span[@id='priority-val']/text()")[1].strip()
        # yanzhengdu = parseHtml.xpath("//div[@id='customfield_10011-val']/text()")[0].strip()
        status = parseHtml.xpath('//*[@id="status-val"]/span/text()')[0].strip()
        # createtime = parseHtml.xpath("//dl[3]//dd[1]/@title")[0].strip() # ICAS使用方式
        createtime = parseHtml.xpath("//div[@id='datesmodule']//dl[1]//dd[1]/@title")[0].strip() # Asterix使用方式
        assignee = parseHtml.xpath("//span[@id='assignee-val']/span[@class='user-hover']/text()")[1].strip()

        self.tittle.append(tittle)
        self.lever.append(lever)
        self.status.append(status)
        self.createtime.append(createtime)
        self.assignee.append(assignee)
        self.cause.append('无分析')

        if assignee in self.VWM_list:
            self.Responsible_party.append('VWM')
        elif assignee in self.Mobvoi_list:
            self.Responsible_party.append("Mobvoi")
        elif assignee == 'LG':
            self.Responsible_party.append("LG")
        else:
            self.Responsible_party.append("NULL")
            print('获取责任方失败，请手动修改！')



    def run(self):
        itext = input("请确认已创建文件 “1.xls” ，并确保格式正确，按回车运行脚本：")

        # time.struct_time(tm_year=2016, tm_mon=4, tm_mday=7, tm_hour=10, tm_min=3, tm_sec=27, tm_wday=3, tm_yday=98, tm_isdst=0)
        xtime = time.localtime()
        tmon = str(xtime.tm_mon)
        tmday = str(xtime.tm_mday)
        thour = str(xtime.tm_hour)
        tmin = str(xtime.tm_min).zfill(2)
        tsec = str(xtime.tm_sec).zfill(2)

        bugkeyList = self.readExcel()
        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet('BugList')
        row_tittle = ['Bug ID','状态','问题','级别','问题原因','经办人','组织','创建日期']

        # 获取单个页面的信息
        for i,n in zip(bugkeyList,range(len(bugkeyList))):
            print("==="+str(n+1)+"："+str(i)+"===")
            bugURL = self.baseURL + str(i)
            print(bugURL + "  >>>>> Done！ \n")
            self.getPage(bugURL)

        # 写入excel的标题
        for t in range(len(row_tittle)):
            worksheet.write(0,t,row_tittle[t])

        for v in range(len(bugkeyList)):
            worksheet.write(v+1,0,bugkeyList[v])
            worksheet.write(v+1,1,self.status[v])
            worksheet.write(v+1,2,self.tittle[v])
            worksheet.write(v+1,3,self.lever[v])
            worksheet.write(v+1,4,self.cause[v])
            worksheet.write(v+1,5,self.assignee[v])
            worksheet.write(v+1,6,self.Responsible_party[v])
            worksheet.write(v+1,7,self.createtime[v])

        # workbook.save('AutoBugList_'+ tmon + tmday + thour + tmin + '.xls')
        workbook.save('AutoBugList_'+ tmin + tsec + '.xls')
        print('AutoBugList_'+ tmin + tsec + '.xls')
        print('Done!')


if __name__ == '__main__':
    spider = JiraBugList()
    spider.run()