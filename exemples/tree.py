#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 GUO DEJIE <dejie.guo@gmail.com>
#
# Distributed under terms of the MIT license.

"""
使用递归，可以绘制出非常复杂的图形。例如，下面的代码可以绘制一棵分型树：
"""
from turtle import *

# 设置颜色模式是RGB：
colormode(255)

lt(90)

lv = 14
l = 120
s = 45

width(lv)

# 初始化RGB颜色：
r = 0
g = 0
b = 0
pencolor(r, g, b)

penup()
bk(l)
pendown()
fd(l)

def draw_tree(l, level):
    global r, g, b
    # save the current pen width
    w = width()

    # narrow the pen width
    width(w * 3 / 4)
    # set color:
    r += 1
    g += 2
    b += 3
    pencolor(r%200, g%200, b%200)

    l *= 3/4

    lt(s)
    fd(l)

    if level < lv:
        draw_tree(l, level+1)
    bk(l)
    rt(2 * s)
    fd(l)

    if level < lv:
        draw_tree(l, level+1)
    bk(l)
    lt(s)

    # restore the previous pen width
    width(w)

speed('fastest')

draw_tree(l, 4)
done()
