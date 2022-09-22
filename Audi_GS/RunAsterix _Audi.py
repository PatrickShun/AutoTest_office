import uiautomator2 as u2
from time import sleep
import xlrd
import sys



class AutoGlobalSearch():

    def __init__(self):
        print("====== Run to Porsche GlobalSearch AutoTest! =====")
        print("!请确认高德、智慧加油、停车、娱乐应用的用户协议已同意！")
        input("!按任意键继续！")

        self.Bench_IP = "172.16.250.248:5555"

        try:
            self.d = u2.connect(self.Bench_IP)
            print("Bench connect Success!")
            self.d.press('home')
            sleep(1)
            self.d.swipe(550, 375, 1053, 375, 0.1)
            sleep(1)
        except Exception as e:
            print("初始化报错!" + e)


    def readExcel(self):
        try:
            data = xlrd.open_workbook("QueryList.xls")
            table = data.sheets()[0]
            tableValueCol = table.col_values(0)
            return tableValueCol
            print(len(tableValueCol))
        except Exception as e:
            print(e)


    def AutoRun(self):

        # 读取Excel内容
        queryList = self.readExcel()

        # 点击一次Global Search进入
        self.d.xpath('//*[@resource-id="com.elektrobit.aed.home.app:id/search_text"]').click()

        try:
            # Audi 点击输入框
            for query in queryList:
                self.d.xpath('//*[@resource-id="com.elektrobit.aed.home.app:id/search_text"]').click()
                sleep(1)

                # 输入queyr
                print("正在搜索【%s】..."%query)
                self.d.send_keys(query, clear=True)
                sleep(1)

                # 点击搜索
                self.d.set_fastinput_ime(False)
                self.d(resourceId="com.elektrobit.aed.home.app:id/icon_search").click()
                sleep(10) # 得改善，判断什么时候返回结果。

                # 截图
                self.d.screenshot(query + ".jpg")
                sleep(1)

        except Exception as fe:
            print(fe)

        input("Done! 点击任意按钮结束。")
        sys.exit()


if __name__ == '__main__':
    RunAuto = AutoGlobalSearch()
    RunAuto.AutoRun()

