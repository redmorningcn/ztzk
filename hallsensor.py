import ctypes
import threading
import time
import zkzt2_com2


if __name__=="__main__":
    if platform.system() == "Linux":
        port = "/dev/ttyUSB0"
        #port = "/dev/ttyUSB1"
    else:
        port  = "COM10"

    pin     = 21
    
    motor   = Zkzt2Data(port)
    Frqer.initFrq(pin)        #频率检测电路引脚

    tfrq    = threading.Thread(target = Frqer.threadCounter)
    #tfrq.start()             #启动多线程

    tsec    = threading.Thread(target = taskSecond)
    #tsec.start()
    
    while True:
        print("输入速度：")
        speed = int(input())
        print("输入频率")
        fre = int(input())
        motor.setSpeed(speed,fre,STA_CCW)    