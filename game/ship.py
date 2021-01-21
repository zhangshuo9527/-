# 开发时间：2021/1/18 10:58
import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        """初始化飞船并设置其初始位置"""
        super(Ship,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('D:\pycharm\py.1\game\source\ships.png')
        self.rect = self.image.get_rect()
        #加载飞船图像并获取其外接矩形
        self.screen_rect = screen.get_rect()
        #将每艘新飞船放在屏幕底部中央
        #飞船中心点横坐标x=
        self.rect.centerx = self.screen_rect.centerx
        #飞船中心点横坐标y=
        self.rect.bottom = self.screen_rect.bottom

        #在飞船的属性center中存储小数值
        self.centers = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def update(self):
        """根据移动标志调整飞船位置"""
        #更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centers += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.centers -= self.ai_settings.ship_speed_factor

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor

        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.ship_speed_factor


        #根据self.center更新rect对象
        self.rect.centerx = self.centers
        self.rect.centery = self.centery
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)
    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.centers = self.screen_rect.centerx

        self.centery = self.screen_rect.bottom - 40
