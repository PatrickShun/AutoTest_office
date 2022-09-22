import uiautomator2 as u2
import PageXpath

class PorscheRunning():

    def __init__(self):
        # self.benchIP = "172.16.250.248:5555"
        self.bench = u2.connect("172.16.250.248:5555")
        # print(bench.info)
        self.bench.press("home")
        self.bench.implicitly_wait(3)


    def setWeatherWidget(self):
        # 判断当前页面是否有weathetWidget.
        try: # 如果没有,执行下一步,如果有则返回Ture.
            print("1")
            self.bench(resourceId = PageXpath.Home_SamllWeather_Cover_resourceId).click()
            print("2")
                
        except:
            print("PageXpath.Home_MeddleWeather_widget_click ERROR")
            print("3")
            try:
                # 1.长按进入编辑模式
                self.bench.long_click(1032, 338)
                print("4")

                # 2.点击中号widget进入选择列表.
                self.bench.xpath(PageXpath.EditMode_ModeThree_Middle).click()
                print("5")

                # 3.点击中号天气widget
                self.bench(text = "天气").click()
                print("6")

                # 4.点击完成.
                self.bench.xpath(PageXpath.EditMode_DoneButton).click()
                print("7")

            except:
                self.bench.press("home")
                print("Set Weather Widget ERROR")

    def Modelpanduan(self):
        try:
            # self.bench.long_click(1032, 338)
            if self.bench(text='地图模式').exists():
                print(1)
            else:
                print(2)
        except:
            print("error")


        


if __name__ == "__main__":
    irunning = PorscheRunning()
    # irunning.setWeatherWidget()
    irunning.Modelpanduan()


