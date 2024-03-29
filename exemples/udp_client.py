#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 GUO DEJIE <dejie.guo@gmail.com>
#
# Distributed under terms of the MIT license.

"""
UDP客户端
"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据：
    s.sendto(data, ('127.0.0.1', 9999))
    # 接收数据：
    print(s.recv(1024).decode('utf-8'))
s.close()
