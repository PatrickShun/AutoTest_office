import uiautomator2 as u2
from time import sleep
# import xlrd
import sys

# com.ticauto.Weather

class AutoWeather():

    def __init__(self):

        print("====== Run to Porsche Weather AutoTest! =====")

        input("!按任意键继续！")

        self.Bench_IP = "172.16.250.248:5555"

        try:
            self.d = u2.connect(self.Bench_IP)
            self.d.debug = True
            self.d.healthcheck()
            print("Bench connect Success!")

            self.d.press('home') # 初始化，每次运行都回到主页
            sleep(1)

            # self.d.swipe(1200, 338, 300, 338, 0.1) #滑动，从x1200y338到x300y338，速度0.1s。 
            # sleep(1)

            print("打印的基本信息：",self.d.info) # 打印基本信息
            # print(self.d.current_app()) # 获取当前应用程序信息
            # print(self.d.serial) # 获取当前设备的序列号
            # print(self.d.wlan_ip) # 获取当前设备的WIFI IP
            # print(self.d.device_info) # 获取当前设备的详细信息

        except Exception as e:
            print("初始化报错!" + e)


    def enterWeather(self):
        try:
            # 启动应用
            # self.d.app_start("com.ticauto.weather/.WeatherContainerActivity") # 不知道为什么无法用这种方式启动
            self.d(resourceId="com.ticauto.weather:id/weather_layout").click() # 只能通过点击页面的元素进入，如果页面没有天气的widget则会报错。
            print("Successful entry weather!")

        except Exception as e:
            print("天气应用打开失败！")
            print(e)



    def addCities(self):
        try:
            pass
            # print(self.d.current_app())
        except:
            print("error")






    def irun(self):
        self.enterWeather() # 进入天气应用
        self.addCities() # 添加城市

        print("Done!")


if __name__ == "__main__":
    RunAutoWeather = AutoWeather()
    RunAutoWeather.irun()