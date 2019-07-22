# -*- coding：utf-8 -*-
# Author：wu 
# Time: 2018年11月05日 20:15

# 存储《外星人入侵》所有船的类

import pygame

class Ship():
    def __init__(self, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('/Users/wackwu/Desktop/Python/Game/Alien_invasion/images/ship.bmp')
        self.rect = self.image.get.rect()
        self.screen_rect = screen.get.rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)