import sys
import pygame

def run_game():
    pygame.init()                                   #初始化背景
    screen = pygame.display.set_mode((1200,800))    #创建名为screen的显示窗口，所有图形元素都将在其中绘制。1200和800是窗体尺寸。
    pygame.display.set_caption('Alien Invasion')    #窗体标题
    bg_color = (230,230,230)                        #设置背景色，RGB值。

    while True:
        for event in pygame.event.get():            #事件循环
            if event.type == pygame.QUIT:           #点击窗口的关闭按钮时，会检测到pygame.QUIT事件。
                sys.exit()                          #调用sys.exit()来退出游戏。
        screen.fill(bg_color)                       #用背景色填充屏幕。screen.fill()只接受一个实参，一种颜色
        pygame.display.flip()                       #更新屏幕

run_game()

