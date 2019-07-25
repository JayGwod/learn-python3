#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 GUO DEJIE <dejie.guo@gmail.com>
#
# Distributed under terms of the MIT license.

"""
使用Tkinter十分简单，我们来编写一个GUI版本的“Hello, world!”。
"""
from tkinter import *
import tkinter.messagebox as messagebox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.expression = Entry(self)
        self.expression.pack()
        self.alertButton = Button(self, text='Evaluate it!', command=self.compute)
        self.alertButton.pack()

    def compute(self):
        expression = self.expression.get() or '0'
        messagebox.showinfo('Result', '%s = %s' % (expression, eval(expression)))


app = Application()
# 设置窗口标题：
app.master.title("Calculator")
# 主消息循环：
app.mainloop()
