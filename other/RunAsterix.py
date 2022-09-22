import uiautomator2 as u2
from time import sleep
import xlrd



class AutoGlobalSearch():

    def __init__(self):
        print("请确认高德、智慧加油、停车、娱乐应用的用户协议已同意！")
        input("按任意键继续！")

        self.Bench_IP = "172.16.250.248:5555"

        try:
            self.d = u2.connect(self.Bench_IP)
            print("Bench connect Succsu!")
        except Exception as e:
            print(e)


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
        # self.d.press('home')
        queryList = self.readExcel()

        # Audi
        for query in queryList:
            self.d.xpath('//*[@resource-id="com.elektrobit.aed.home.app:id/search_text"]').click()
            sleep(1)
            # 输入queyr
            self.d.send_keys(query, clear=True)
            sleep(1)

            # 点击搜索
            self.d.set_fastinput_ime(False) #禁用原生键盘
            self.d.xpath('//*[@resource-id="com.elektrobit.aed.home.app:id/icon_search"]').click()
            sleep(3)

            # 截图
            self.d.screenshot(query + ".jpg")
            sleep(2)


if __name__ == '__main__':
    RunAuto = AutoGlobalSearch()
    RunAuto.AutoRun()

