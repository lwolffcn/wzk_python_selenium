#coding=utf-8
import tkinter as tk
# from tkinter import *


def resize(ev=None):
    hello_label.config(font='Helvetica %d bold' % scale.get())


top = tk.Tk()
top.geometry('250x150')

hello_label = tk.Label(top, text='hello', font='Helvetica -12 bold')
hello_label.pack(fill=tk.Y,expand=1)

scale = tk.Scale(top, from_=10, to=80, orient=tk.HORIZONTAL, command=resize)
scale.set(12)
scale.pack(fill=tk.X,expand=1)

quit_button = tk.Button(top, text='QUIT', command=top.quit, activeforeground='white', activebackground='red')
quit_button.pack(fill=tk.X, expand=1)

tk.mainloop()  # 进入前述的无限主循环
