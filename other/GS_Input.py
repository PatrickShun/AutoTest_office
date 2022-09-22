import uiautomator2 as u2
from time import sleep
from tkinter import *

# 初始化：python -m uiautomator2 init

input("(请确认运行环境,并运行命令:python -m uiautomator2 init)")

def GS_input():
    # 获取输入的文案
    GS_query = ent1.get()


    # 输入文本
    d.xpath('//*[@resource-id="com.elektrobit.aed.home.app:id/search_text"]').click()
    d.send_keys(GS_query,clear=True)
    sleep(0.5)
    # 切换成 ui2 的输入法，这里会隐藏掉系统原本的输入法 , 默认是使用系统输入法
    # 当传入 False 时会使用系统默认输入法，默认为 Fasle
    d.set_fastinput_ime(False)
    # d.current_ime()
    # d.press('enter')
    # d.keyevent('enter')


    print("输入【%s】 Done!！"%GS_query)

d =  u2.connect("172.16.250.248:5555")

# d.press('home')

# 创建TK
root = Tk()

# 保存变量
GS_input_text = StringVar()

# 标题
Label(root,text="GS_query:").grid(row=0,column=0,padx=5,pady=5)


# 输入框
ent1 = Entry(root,width=50)
ent1.grid(row=0,column=1,padx=5,pady=5)


# 按钮
Button(root,text="确认",width=10,command=GS_input).grid(row=1,column=0,padx=5,pady=5,sticky=W)
Button(root,text="退出",width=10,command=root.quit).grid(row=1,column=1,padx=5,pady=5,sticky=E)


mainloop()