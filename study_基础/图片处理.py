#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/16 下午5:38
# @File    : 图片处理.py
from PIL import Image
img = Image.open('/Users/Tong/Desktop/1.png')
print("存储格式：%s  尺寸：%s  模式：%s  "%(img.format,img.size,img.mode))
img.thumbnail((720, 300))
img.save('/Users/Tong/Desktop/2.png', 'JPEG')