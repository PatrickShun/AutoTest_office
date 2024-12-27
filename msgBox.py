import os
import re
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import subprocess

# 全局变量
audio_directory = ""
audio_files = []
current_audio_index = 0
play_exe = 'C:\\Program Files (x86)\\VideoLAN\\VLC\vlc.exe'

# 播放音频的函数
def play_audio(file_path):
    subprocess.call([play_exe, file_path], stdout=subprocess.PIPE)

# 选择音频目录
def select_audio_directory():
    global audio_directory, audio_files
    audio_directory = filedialog.askdirectory()
    if audio_directory:
        audio_files = [os.path.join(audio_directory, file) for file in os.listdir(audio_directory) if file.endswith('.wav')]
        audio_files.sort()  # 按文件名排序
        current_audio_index = 0
        messagebox.showinfo("成功", "音频目录选择成功")

# 读取音频文件
def read_audio_files():
    global audio_files
    if audio_directory:
        messagebox.showinfo("成功", f"找到 {len(audio_files)} 个音频文件")
    else:
        messagebox.showwarning("警告", "请先选择音频目录")

# 播放下一条音频
def play_next_audio():
    global current_audio_index
    if 0 <= current_audio_index < len(audio_files):
        play_audio(audio_files[current_audio_index])
        current_audio_index += 1
    else:
        messagebox.showwarning("警告", "没有更多的音频文件了")

# 获取日志信息
def get_log_info():
    # 这里需要替换成您获取日志信息的实际命令
    command = "adb logcat"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # 等待一段时间以确保日志信息被收集
    process.wait(timeout=5)  # 等待5秒，根据需要调整
    
    # 获取输出
    stdout, stderr = process.communicate()
    
    # 使用正则表达式匹配日志信息
    pattern = r"SPEECH_DEI: \[NGC_E2E\]"
    matches = re.findall(pattern, stdout)
    
    if matches:
        messagebox.showinfo("日志信息", "\n".join(matches))
    else:
        messagebox.showinfo("日志信息", "没有找到匹配的日志信息")

# 创建主窗口
root = tk.Tk()
root.title("音频日志工具")

# 创建按钮
select_dir_button = tk.Button(root, text="选择音频目录", command=select_audio_directory)
select_dir_button.pack()

read_audio_button = tk.Button(root, text="读取音频", command=read_audio_files)
read_audio_button.pack()

next_audio_button = tk.Button(root, text="下一条", command=play_next_audio)
next_audio_button.pack()

get_log_button = tk.Button(root, text="获取日志信息", command=get_log_info)
get_log_button.pack()

# 运行主循环
root.mainloop()