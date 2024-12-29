import os, re
import tkinter as tk
import pandas as pd
import subprocess
from tkinter import filedialog, messagebox
from time import sleep
from datetime import datetime


# VLC 可执行文件路径 (根据实际路径修改)
VLC_PATH = r"D:\\install\\VLC\\vlc.exe"  # 请确保此路径指向正确的 VLC 可执行文件
wakeUp = r"D:\\02_code\\AudioFile\\00_你好小P.wav"
quitVoice = r"D:\\02_code\\AudioFile\\01_退下吧小P.wav"



# 定义全局变量
audio_files = []
current_audio_index = 0
log_data = []
match_query = "null"
match_msgid = "null"

# 获取当前时间
current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
file_path = f"MsgID_Result{current_time}.xlsx"


# 解析logcar的日志获取msg与query
def get_msgANDquery(def_log_file):
    global match_query, match_msgid
    for line in def_log_file:                           # 逐行读取
        pattern_log = r"SPEECH_DEI: \[NGC_E2E\].*"          # 使用正则表达式匹配指定日志字段
        matches_log = re.findall(pattern_log, line)             # 获取匹配正确的所有数据

        pattern_query = r'"query":"(.*?)"'
        pattern_msgid = r"\[NGC_E2E\]\[(.*?)\]"
        
        # 使用 re.findall() 查找所有匹配的内容
        matches_query = re.findall(pattern_query, line)
        matches_msgid = re.findall(pattern_msgid, line)
            
        # 打印所有匹配的字符串
        for match1,match2 in zip(matches_query,matches_msgid):
            print(match1,match2)

    match_query = matches_query[-1]
    match_msgid = matches_msgid[-1]

    print(f"match resutl:{match_query}, {match_msgid}")


# 获取安卓日志的函数
def get_log():
    # 使用 adb pull 拉取日志文件到本地
    log_file_path = "main.txt"
    # subprocess.run(["adb", "pull", "/data/Log/log0/main.txt", log_file_path])
    
    # 读取拉取到的日志文件
    try:
        with open(log_file_path, "r", encoding="utf-8", errors="ignore") as log_file:
            get_log_data = log_file.read()

    except UnicodeDecodeError:
        # 如果使用utf-8失败，可以尝试其他编码
        with open(log_file_path, "r", encoding="ISO-8859-1", errors="ignore") as log_file:
            get_log_data = log_file.read()

    pattern = r"SPEECH_DEI: \[NGC_E2E\].*"          # 使用正则表达式匹配指定日志字段
    matches = re.findall(pattern, get_log_data)     # 获取匹配正确的所有数据
    get_msgANDquery(matches)

    return matches

# 读取目录下的所有音频文件
def load_audio_files(directory):
    global audio_files
    audio_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(('.mp3', '.wav', '.ogg'))]
    update_audio_listbox()

# 更新音频列表
def update_audio_listbox():
    global scrollbar
    audio_listbox.delete(0, tk.END)  # 清空列表
    for file in audio_files:
        audio_listbox.insert(tk.END, os.path.basename(file))  # 只显示文件名，不显示完整路径
    # 更新滚动条
    scrollbar.set(0, 1)  # 自动调整滚动条的位置

# 播放音频的函数
def play_audio():
    global current_audio_index, audio_files, audio_listbox
    if not audio_files:
        messagebox.showerror("错误", "没有音频文件可以播放")
        return
    
    # 清除日志
    # subprocess.run(["adb", "logcat", "-c"])
    # 等待 1 秒
    # sleep(1)
    if current_audio_index < len(audio_files):
        sleep(1)
        # 获取音频路径, 并替换反斜杠为正斜杠
        audio_file = audio_files[current_audio_index]
        audio_file = audio_file.replace("/", "\\")
        audio_nema = os.path.basename(audio_file)
        audio_state = audio_nema.split("_")[1]
        print(f"正在播放：{audio_file}")
        
        # 使用 VLC 播放音频文件
        if audio_state == "3":
            subprocess.run([VLC_PATH, quitVoice, "--play-and-exit"])    # 播放之前先退出小P
            subprocess.run([VLC_PATH, audio_file, "--play-and-exit"])   # "--play-and-exit" 参数表示播放完毕后退出 VLC
        elif audio_state == "4":
            subprocess.run([VLC_PATH, audio_file, "--play-and-exit"])
        elif audio_state == "5":
            subprocess.run([VLC_PATH, quitVoice, "--play-and-exit"])     # 播放之前先退出小P
            subprocess.run([VLC_PATH, wakeUp, "--play-and-exit"])        # 播放唤醒词
            subprocess.run([VLC_PATH, audio_file, "--play-and-exit"]) 
    else:
        messagebox.showinfo("提示", "已播放完所有音频")

# 获取并显示日志
def display_log():
    global current_audio_index
    log_matches = get_log()
    if log_matches:
        log_output = "\n".join(log_matches)
        log_display.config(state=tk.NORMAL)
        log_display.delete(1.0, tk.END)
        log_display.insert(tk.END, log_output)
        log_display.config(state=tk.DISABLED)
    else:
        messagebox.showinfo("提示", "没有匹配到日志")

    # 显示msgID 和 query
    if match_query:
        query_entry.config(state=tk.NORMAL)       # 允许编辑
        query_entry.delete(0, tk.END)             # 清空内容
        query_entry.insert(tk.END, match_query)   # 设置为正则获取到的query
        query_entry.config(state=tk.DISABLED)     # 设置为只读

    if match_msgid:
        megid_entry.config(state=tk.NORMAL)       # 允许编辑
        megid_entry.delete(0, tk.END)             # 清空内容
        megid_entry.insert(tk.END, match_msgid)   # 设置为正则获取到的msgid
        megid_entry.config(state=tk.DISABLED)     # 设置为只读

# 选择音频目录
def select_directory():
    directory = filedialog.askdirectory(title="选择音频目录")
    if directory:
        load_audio_files(directory)
        messagebox.showinfo("提示", f"已加载 {len(audio_files)} 个音频文件")

# 播放选中音频按钮的回调函数
def play_selected_audio():
    global current_audio_index
    selected_index = audio_listbox.curselection()
    if selected_index:
        current_audio_index = selected_index[0]
        play_audio()

# 下一条音频按钮的回调函数
def next_audio():
    global current_audio_index
    selected_index = audio_listbox.curselection()
    if selected_index:
        current_audio_index += 1

        # 更新列表框中的选中效果
        audio_listbox.selection_clear(0, tk.END)  # 清除之前的选中项
        audio_listbox.selection_set(current_audio_index)  # 设置当前音频为选中项
        audio_listbox.activate(current_audio_index)  # 激活当前音频

        play_audio()

# 保存到 Excel
def save_to_excel():
    # 获取音频文件，Query，MsgID，日志内容
    audio_file_name = os.path.basename(audio_files[current_audio_index]) if audio_files else "N/A"
    query_content = query_entry.get() if query_entry.get() else "N/A"
    megid_content = megid_entry.get() if megid_entry.get() else "N/A"
    log_content = log_display.get("1.0", tk.END).strip() if log_display.get("1.0", tk.END).strip() else "N/A"

    # 创建 DataFrame
    data = {
        "音频文件": [audio_file_name],
        "Query": [query_content],
        "MsgID": [megid_content],
        "日志": [log_content]
    }
    df = pd.DataFrame(data)

    # 检查文件是否存在
    if os.path.exists(file_path):
        # # 如果文件存在，打开文件并追加数据
        # with pd.ExcelWriter(file_path, mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
        #     df.to_excel(writer, index=False, header=False, sheet_name='Sheet1')  # 不写入表头，追加数据

        # 如果文件存在，先读取原有数据
        existing_df = pd.read_excel(file_path, engine='openpyxl')
        # 追加新的数据
        updated_df = pd.concat([existing_df, df], ignore_index=True)
        # 将合并后的数据保存回 Excel，避免重复写入表头
        with pd.ExcelWriter(file_path, mode='w', engine='openpyxl') as writer:
            updated_df.to_excel(writer, index=False, header=True, sheet_name='Sheet1')
            
    else:
        # 如果文件不存在，创建新文件并写入数据
        df.to_excel(file_path, index=False, engine='openpyxl')

    # 更新 save_path_label 显示文件路径
    save_current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    save_path_label.config(text=f"保存路径: {file_path}  <<{save_current_time}>>",fg="green")


# 创建界面
def create_gui():
    global audio_listbox, log_display, megid_entry, query_entry, save_path_label, file_path, scrollbar

    window = tk.Tk()
    window.title("=== MsgID获取工具 ===")

    # 创建左侧框架（按钮区域）
    left_frame = tk.Frame(window)
    left_frame.grid(row=0, column=0, rowspan=2, padx=10, pady=10, sticky="nswe")

    # 创建按钮
    button_width = 18  # 按钮宽度统一
    select_button = tk.Button(left_frame, text="选择音频目录", command=select_directory, width=button_width)
    select_button.grid(row=0, column=0, pady=5, sticky="ew")

    play_button = tk.Button(left_frame, text="Play", command=play_selected_audio, width=button_width)
    play_button.grid(row=1, column=0, pady=5, sticky="ew")

    next_button = tk.Button(left_frame, text="下一条", command=next_audio, width=button_width)
    next_button.grid(row=2, column=0, pady=5, sticky="ew")

    log_button = tk.Button(left_frame, text="获取日志信息", command=display_log, width=button_width)
    log_button.grid(row=3, column=0, pady=5, sticky="ew")

    save_button = tk.Button(left_frame, text="保存到Excel", command=save_to_excel, width=button_width)
    save_button.grid(row=4, column=0, pady=5, sticky="ew")

    # 显示文件保存路径
    # save_path_label = tk.Label(left_frame, text="文件保存路径: ", width=button_width)
    # save_path_label.grid(row=5, column=0, pady=10, sticky="ew")

    # 创建中间框架（音频列表区域）
    center_frame = tk.Frame(window)
    center_frame.grid(row=0, column=1, padx=10, pady=5, sticky="nswe")

    # 创建并配置垂直滚动条
    scrollbar = tk.Scrollbar(center_frame, orient="vertical")

    # 音频文件列表
    audio_listbox = tk.Listbox(center_frame, width=30, height=15, selectmode=tk.SINGLE,yscrollcommand=scrollbar.set)
    audio_listbox.grid(row=0, column=0, sticky="nsew") 

    # 配置滚动条
    scrollbar.config(command=audio_listbox.yview)  # 将滚动条与 listbox 绑定
    scrollbar.grid(row=0, column=1, sticky="ns")  # 将滚动条放在右侧，纵向

    # 创建右侧框架（日志显示区域）
    right_frame = tk.Frame(window)
    right_frame.grid(row=0, column=2, padx=5, pady=10, sticky="nswe")

    # 显示日志的区域
    log_display = tk.Text(right_frame, height=20, width=60, wrap=tk.WORD, state=tk.DISABLED)
    log_display.grid(row=0, column=0, sticky="nsew")  # 占用右侧框架

    # 左下部分框架
    left_frame = tk.Frame(window)
    left_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=10, sticky="nswe")

    # 显示文件保存路径（跨越左中部分）
    save_path_name = "结果保存：" + file_path
    save_path_label = tk.Label(left_frame, text=save_path_name)
    save_path_label.grid(row=0, column=0, pady=5, sticky="ew")

    # 右下部分框架（MegID 和 Query 控件）
    right_bottom_frame = tk.Frame(window)
    right_bottom_frame.grid(row=1, column=2, padx=5, pady=10, sticky="nswe")

    # MegID 显示框架
    megid_label = tk.Label(right_bottom_frame, text="MegID:")
    megid_label.grid(row=0, column=0, padx=5)

    megid_entry = tk.Entry(right_bottom_frame, width=40, state='readonly')
    megid_entry.grid(row=0, column=1, padx=5)

    # Query 显示框架
    query_label = tk.Label(right_bottom_frame, text="Query:")
    query_label.grid(row=1, column=0, padx=5)

    query_entry = tk.Entry(right_bottom_frame, width=40, state='readonly')
    query_entry.grid(row=1, column=1, padx=5)

    # 配置窗口的列和行权重，使得布局适应窗口大小调整
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=2)
    window.grid_columnconfigure(2, weight=1)

    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1)

    window.mainloop()


if __name__ == "__main__":
    create_gui()