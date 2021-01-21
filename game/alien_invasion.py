# 开发时间：2021/1/18 9:47
import sys
import pygame
from pygame.sprite import Group
from ship import Ship
from alien import Alien
import game_functions as gf
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button


def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建Play按钮
    play_button = Button(ai_settings,screen,"Play")
    #创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)
    #创造一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    #创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)
    #播放背景音乐
    pygame.mixer.music.load('D:\pycharm\py.1\game\source\music.mp3')
    pygame.mixer.music.play(-1)  # 重复播放
    #开始游戏的主循环
    while True:
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,
            play_button)

run_game()