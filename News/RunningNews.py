import requests
from time import sleep
from lxml import etree
import random as R
# from alive_progress import alive_bar

# 中国新闻网
baseURL = "https://www.chinanews.com.cn/scroll-news/news1.html"
# headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'}

NewsLeixing = {
"cj":"财经",
"tp":"图片",
"shipin":"视频",
"tw":"台湾",
"gj":"国际",
"gn":"国内",
"sh":"社会",
"":"",
}

# xpath = "/html/body/div[4]/div[1]/div[2]/ul/li/div[2]/a/@href"
headersList =[{'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'},
              {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
              {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'},
              {'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)'},
              {'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)'},
              {'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}]

def GetNewsList():
    headers = R.choice(headersList)
    res = requests.get(baseURL,headers=headers)
    res.encoding = "utf-8"
    html = res.text
    parseHtml = etree.HTML(html)
    NewsUrlList = parseHtml.xpath("/html/body/div[4]/div[1]/div[2]/ul/li/div[2]/a/@href")
    return NewsUrlList


def SaveNewList(NewList):
    f = open("NewsURLList.txt","w+",encoding="utf-8")
    for i in range(len(NewList)):
        writeURL = "https://www.chinanews.com.cn" + NewList[i] + "\n"
        f.write(str(writeURL))

    print("保存中.......")
    sleep(1)
    f.close()


def ReadNewList():
    rd_List = []
    with open("NewsURLList.txt","r",encoding="utf-8") as rf:
        for line in rf:
            rd_List.append(list(line.strip('\n').split(',')))

    return rd_List


def GetNewDetails(G_URL):
    # 请求新闻详情
    headers = R.choice(headersList)
    print("Headers:",headers)
    res1 = requests.get(G_URL,headers=headers)
    res1.encoding = "utf-8"
    html1 = res1.text
    parseHtml1 = etree.HTML(html1)

    try:
        try:
            title = parseHtml1.xpath('/html/body/div[4]/div/div[1]/div[1]/h1/text()')
            zhengwen1 = "Detail is null!"
            print(title[0])
            print(zhengwen1)
            print("最内层获取成功！正在写入...")
            writeNewDetails(title[0],zhengwen1)
        except:
            print("内层获取失败！")
            # 输出标题
            title = parseHtml1.xpath('//*[@id="cont_1_1_2"]/div[2]/h1/text()')
            zhengwen = parseHtml1.xpath('//*[@id="cont_1_1_2"]/div[2]/div[4]/div/p/text()')

            # for i in range(len(zhengwen)):
            #     print(zhengwen[i].strip("").strip(":"))    
            zhengwen1 = "\n".join(zhengwen)

            print(title[0])
            print("外层获取成功！正文已保存！")
            
            # 保存
            writeNewDetails(str(title[0]),zhengwen1)

    except:  # 如果匹配不到正文内容，则以另一种方式匹配获取标题即可。
        title = "Title is null!"
        zhengwen1 = "Detail is null!"
        print(title)
        print(zhengwen1)
        print("连外层都获取失败了，保存占位符！")
        # 异常保存，占位
        writeNewDetails(title,zhengwen1)


def writeNewDetails(NewsTitle,NewsText):
    with open(r"NewsDetailText.txt","a",encoding="utf-8") as ff:
        ff.write(NewsTitle)
        ff.write("\n")
        ff.write(NewsText)
        ff.write("\n")
        ff.write("="*30)
        ff.write("\n")
        sleep(1)
        ff.close()


def RunToNewsList():
    NLits = GetNewsList()
    SaveNewList(NLits)


def RunToNewDetla():
    RList = ReadNewList()
    BList = len(RList)
    for i in range(20):
        sleepTime = R.randrange(2,8)
        print("==↓↓=="*15)
        print("sleepTime：",sleepTime)
        sleep(int(sleepTime))
        detailsURL = RList[i][0]
        print(detailsURL)
        GetNewDetails(detailsURL)
        print("==END=="*15,"\n")

if __name__ == "__main__":
    print("Start running...")

    minling = input("需要运行哪个步骤, 按1获取新闻列表, 按2获取新闻详情：")
    
    if minling == "1":
        RunToNewsList() # 获取新闻列表
    else:
        RunToNewDetla() # 获取新闻详情
        print("Done!")

    print("Finish!")

