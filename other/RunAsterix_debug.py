import uiautomator2 as u2
from time import sleep
import xlrd

# 初始化：python -m uiautomator2 init

d = u2.connect('172.16.250.248:5555')

query = ["双色球的中奖结果","北京去上海的航班","上海的天气"]

# print(d.info)
d.press('home')
sleep(1)

# 滑动
# d.swipe(sx, sy, ex, ey, 0.5) # 开始点是（sx，sy），结束点是（ex,ey),从开始滑动到结束，速度是0.5s
d.swipe(1200, 338, 300, 338, 0.1)


# 点击键盘搜索
# d.click(1582, 658)

# 点击输入框,进入GS
d(resourceId="com.elektrobit.aed.home.app:id/search_bar_text").click()


# 点击天气应用
# d.xpath('//*[@resource-id="com.ticauto.weather:id/weather_cover"]').click()


# 输入文本
# d.xpath('//*[@resource-id="com.elektrobit.aed.home.app:id/search_layout"]/android.widget.FrameLayout[2]').click()
# d.send_keys("今天上海的天气", clear=True)

# Audi
# d.xpath('//*[@resource-id="com.elektrobit.aed.home.app:id/search_text"]').click()
# sleep(1)

for q in query:
    # 点击输入框
    d.xpath('//*[@resource-id="com.elektrobit.aed.home.app:id/search_text"]').click()

    # 输入query
    print("正在搜索【%s】..."%q)
    d.send_keys(q, clear=True)
    sleep(1)

    # 点击搜索
    d.set_fastinput_ime(False)
    d(description="搜索").click()
    sleep(15)

    # 截图
    d.screenshot(q + ".jpg")
    sleep(2)



# data = xlrd.open_workbook("QueryList.xls")
# table = data.sheets()[0]
# tableValueCol = table.col_values(0)
# print(len(tableValueCol))
# for i in tableValueCol:
#     print(i)

print("Done!")