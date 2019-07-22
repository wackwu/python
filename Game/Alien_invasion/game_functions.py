# -*- coding：utf-8 -*-
# Author：wu 
# Time: 2018年11月7日 17:13

# 存储游戏运行函数


import sys
import pygame

def check_events():
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            sys.exit()