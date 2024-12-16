import os
import tkinter as tk
from tkinter import messagebox, simpledialog
import pyperclip
import random

def get_user_folder():
    # 获取用户文件夹路径
    return os.path.expanduser("~")

def get_file_path():
    # 定义文件路径
    user_folder = get_user_folder()
    file_path = os.path.join(user_folder, "words.txt")
    return file_path

def count_words_in_file():
    # 统计文件中的词汇数量
    file_path = get_file_path()
    if not os.path.exists(file_path):
        return 0
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    return len(lines)

def write_words_to_file(words):
    # 写入词汇到文件
    file_path = get_file_path()
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(words + "\n")

def read_and_remove_word():
    # 读取并移除一个词汇
    file_path = get_file_path()
    if not os.path.exists(file_path):
        return None

    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    if not lines:
        return None

    word = random.choice(lines).strip()  # 随机选择一行词汇
    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines([line for line in lines if line.strip() != word])

    return word

def refresh_word_count(label):
    # 刷新词汇数量显示
    word_count = count_words_in_file()
    label.config(text=f"当前数量：{word_count}")

def add_words(event=None):
    # 添加词汇
    words = add_entry.get()
    if words:
        write_words_to_file(words)
        add_entry.delete(0, tk.END)
        refresh_word_count(word_count_label)

def extract_word():
    # 提取词汇
    word = read_and_remove_word()
    if word:
        pyperclip.copy(word)  # 将提取的词汇复制到剪贴板
        word_label.config(text=f"提取的词汇是：{word}")
        refresh_word_count(word_count_label)
    else:
        word_label.config(text="没有可提取的词汇！")

def open_word_file():
    # 打开词汇文件
    file_path = get_file_path()
    if os.path.exists(file_path):
        os.system(f"notepad.exe {file_path}")  # 使用记事本打开文件
        refresh_word_count(word_count_label)
    else:
        messagebox.showwarning("警告", "词汇文件不存在！")

# 创建主窗口
root = tk.Tk()
root.title("无言天天开心")
root.geometry("400x400")

# 标题标签
title_label = tk.Label(root, text="无言天天开心", font=("Arial", 20), pady=10)
title_label.pack()

# 词汇数量标签
word_count_label = tk.Label(root, text="", font=("Arial", 14))
word_count_label.pack()
refresh_word_count(word_count_label)

# 添加词汇部分
add_frame = tk.Frame(root)
add_frame.pack(pady=10)

add_label = tk.Label(add_frame, text="添加：", font=("Arial", 12))
add_label.grid(row=0, column=0, padx=5, pady=5)

add_entry = tk.Entry(add_frame, font=("Arial", 12), width=20)
add_entry.grid(row=0, column=1, padx=5, pady=5)
add_entry.bind('<Return>', add_words)  # 绑定回车事件

# 提取词汇部分
extract_frame = tk.Frame(root)
extract_frame.pack(pady=10)

extract_button = tk.Button(extract_frame, text="提取", font=("Arial", 12), command=extract_word)
extract_button.pack()

word_label = tk.Label(extract_frame, text="", font=("Arial", 12))
word_label.pack(pady=5)

# 打开词汇文件按钮
open_file_button = tk.Button(root, text="打开txt", font=("Arial", 12), command=open_word_file)
open_file_button.pack(pady=10)

exit_button = tk.Button(root, text="退出程序", font=("Arial", 12), command=root.destroy)
exit_button.pack(pady=10)

# 运行主循环
root.mainloop()
