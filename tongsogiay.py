# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:08:27 2024

@author: ASUS-PC
"""

gio = int(input("Nhập giờ:"))
phut = int(input("Nhập phút:"))
giay = int(input("Nhập giây:"))
tong_giay = gio * 3600 + phut * 60 + giay
print("Tổng số giây là:",tong_giay)
