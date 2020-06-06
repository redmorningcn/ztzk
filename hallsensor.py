import ctypes
import threading
import time
from  zkzt2_com2  import *
from  keyer       import *
#import platform

if __name__=="__main__":
    if platform.system() == "Linux":
        port = "/dev/ttyUSB0"
        #port = "/dev/ttyUSB1"
    else:
        port  = "COM10"

    KEY_SUB    = 13      #速度-
    KEY_ADD    = 5       #速度减
    
    initKey(KEY_SUB)  #初始化速度-按键
    initKey(KEY_ADD)  #初始化速度+按键
    KeyThread = threading.Thread(target = daemonKey)     #创建多线程，启动接收任务
    KeyThread.start()
    
    
    FRQ_IN     = 21      #频率采集    
    Frqer.initFrq(FRQ_IN)        #频率检测电路引脚

    tfrq    = threading.Thread(target = Frqer.threadCounter)
    tfrq.start()             #启动多线程

    tsec    = threading.Thread(target = taskSecond)
    tsec.start()
    
    motor   = Zkzt2Data(port)
    
    fre   = 3000
    speed = 20
    l_speed = 0
    while True:
        #print("输入速度：")
        #speed = int(input())
        #print("输入频率")
        #fre = int(input())
        #time.sleep(1)
        #print("KEY_SUB Value",getKeySta(KEY_SUB))
        
        
        if getKeySta(KEY_SUB) |  getKeySta(KEY_ADD):   #有按键按下
            #print("KEY_SUB | KEY_ADD")
            if getKeySta(KEY_ADD):
                #print("KEY_ADD ")
                if l_speed > 0:
                    speed = l_speed +1
                    if speed > 100:
                        speed = 100
                else:
                    speed = 20   
            else:
                #print("KEY_SUB ")
                if l_speed > 15:
                    speed = l_speed -1
                else:
                    speed   = 0
                    l_speed = 0
                
            l_speed = speed            
        
            motor.setSpeed(speed,fre,STA_CCW)
            time.sleep(1)