# -*- coding：utf-8 -*-
# Author：wu 
# Time: 2018年10月18日 19:30

# 外星人运行主类

import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # 初始化pygame,设置和屏幕的对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(screen)


    # 开始游戏主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_events()

        # 每次循环时都会重绘屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # 让最近绘制的屏幕可见
        pygame.display.flip()

# 运行游戏        
run_game()