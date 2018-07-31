import sys,os                                    #导入os是为了避免sys.exit()抛出的异常
import pygame
from alien import Alien
from bullet import Bullet
from time import sleep                          #sleep用于暂停游戏

def check_keydown_events(event,ai_settings,screen,stats,sb,play_button,ship,aliens,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        if stats.game_active == False:
            start_game(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        else:
            fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        os._exit(0)

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets):
    for event in pygame.event.get():            #用户的所有事件都是通过pygame.event.get()获取的
        if event.type == pygame.QUIT:
            #sys.exit()
            os._exit(0)                         #使用sys.exit()总是抛出异常，所以换成这个。    
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x , mouse_y = pygame.mouse.get_pos()  #mouse.get_pos()返回一个元组，包含点击时鼠标的x和y坐标
            check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)

def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)        #collidepoint检查点击的坐标是否在rect内
    if button_clicked and not stats.game_active:
        start_game(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)

def start_game(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets):
    ai_settings.initialize_dynamic_settings()                               #重置游戏设置
    pygame.mouse.set_visible(False)                                         #隐藏光标
    stats.reset_stats()
    stats.game_active = True

    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()
    sb.prep_ships()

    aliens.empty()
    bullets.empty()
    create_fleet(ai_settings,screen,ship,aliens)
    ship.center_ship()

def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():                        #绘制子弹组
        bullet.draw_bullet()
    ship.blitme()                                           #显示船.
    aliens.draw(screen)                                     #绘制外星人组
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()                                   #刷新屏幕

def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
    bullets.update()                                        #刷新子弹位置，对Group(精灵组)使用update相当于对每隔精灵都使用update  
    for bullet in bullets.copy():                           
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)                          #删除已消失的子弹
    check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets)       #碰撞检测及处理
    


def check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets):
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)   #groupcollide检测碰撞，判断两者rect重叠并返回字典
                                                                        #字典的键为比较者(子弹)，值为一个列表，即被比较者(外星人)，可以多个
                                                                        #在这里，函数会遍历每个子弹和每个外星人
                                                                        #第一个True表示比较者会被删除，第二个True表示被比较者也会被删除
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats,sb)                                      #检查是否超越了最高分
    if len(aliens) == 0:
        bullets.empty()                                                 #empty()会删除所有的子弹(精灵)
        ai_settings.increase_speed()                                                 
        stats.level += 1                                                #等级+1并显示出来
        sb.prep_level()
        create_fleet(ai_settings,screen,ship,aliens)


def fire_bullet(ai_settings,screen,ship,bullets):
    if len(bullets) < ai_settings.bullet_allowed:              #检查屏幕中的子弹是否超过限制数量
        new_bullet = Bullet(ai_settings,screen,ship)           #创建一个Bullet实例
        bullets.add(new_bullet)                                 #加入到编组bullets中

def get_number_aliens_x(ai_settings,alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width          #可用显示范围为屏幕总款-2个外星人的宽度（作为页边距）
    number_aliens_x = int(available_space_x / ( 2 * alien_width) )        #计算一共可以显示多少个外星人
    return number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
    available_space_y = (ai_settings.screen_height-(3*alien_height) - ship_height)
    number_rows = int(available_space_y/(2*alien_height))               #给每行外星人预留2个外星人的高度
    return number_rows

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    alien = Alien(ai_settings,screen)                               #创建外星人实例
    alien_width = alien.rect.width                                  #取得外星人矩形的宽度
    alien.x = alien_width + 2 * alien_width * alien_number          #每个新的外星人向右偏移2个外星人的宽度
    alien.rect.x = alien.x                                          #给每个外星人的最终位置设定x坐标

    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number       #每行新的外星人向下偏移2个外星人的高度
    aliens.add(alien)                                                ###向aliens群组插入新的外星人(精灵)
    #print(len(aliens))

def create_fleet(ai_settings,screen,ship,aliens):
    alien = Alien(ai_settings,screen)                 
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)

def check_fleet_edges(ai_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)      #检测只要有一个外星人达到屏幕边缘，就改变方向值。
            break

def change_fleet_direction(ai_settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings,stats,sb,screen,ship,aliens,bullets):
    if stats.ships_left > 0:
        stats.ships_left -= 1
        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)              #显示光标

def check_aliens_bottom(ai_settings,stats,sb,screen,ship,aliens,bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings,stats,sb,screen,ship,aliens,bullets)
            break

def update_aliens(ai_settings,stats,sb,screen,ship,aliens,bullets):
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens):    #spritecollideany接受一个精灵一个编组。遍历编组找到与精灵碰撞的成员并停止。返回该成员。
        ship_hit(ai_settings,stats,sb,screen,ship,aliens,bullets)
    check_aliens_bottom(ai_settings,stats,sb,screen,ship,aliens,bullets)

def check_high_score(stats,sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()