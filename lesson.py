import schedule
import time
import pygame


def over_class():
    filepath=""

    #初始化
    pygame.mixer.init()

    #加载音乐
    track = pygame.mixer.music.load(filepath)

    #播放音乐
    pygame.mixer.music.play()

    #播放音乐的时间，没有睡眠时间 ，程序一下就会执行完 ，音乐播放不出来
    time.sleep(232)

    #关闭音乐
    pygame.mixer.music.stop()

def start_class():    
    filepath=""

    #初始化
    pygame.mixer.init()

    #加载音乐
    track = pygame.mixer.music.load(filepath)

    #播放音乐
    pygame.mixer.music.play()

    #播放音乐的时间，没有睡眠时间 ，程序一下就会执行完 ，音乐播放不出来
    time.sleep(232)

    #关闭音乐
    pygame.mixer.music.stop()

 
# 当every()没参数时默认是1小时/分钟/秒执行一次job函数

schedule.every().day.at("10:30").do(start_class)
schedule.every().day.at("10:30").do(start_class)
schedule.every().day.at("10:30").do(start_class)
schedule.every().day.at("10:30").do(start_class)
schedule.every().day.at("10:30").do(start_class)

schedule.every().day.at("10:30").do(over_class)
schedule.every().day.at("10:30").do(over_class)
schedule.every().day.at("10:30").do(over_class)
schedule.every().day.at("10:30").do(over_class)
schedule.every().day.at("10:30").do(over_class)

while True:
    # 启动服务
    schedule.run_pending()
    time.sleep(1)
    
    