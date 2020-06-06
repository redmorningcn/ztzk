'''
作者：redmorningcn  20.05.31

函数：daemonKey（）         (按键守护程序，100ms频次，判断按键是否按下)，需多线启动运行
函数：initKey（pinnum）     （初始化指定引脚）
函数：getKeySta(pinnum)    取指定脚状态。0：按键未按下;大于0,按键按下，且值越大，按越久

'''

import RPi.GPIO as GPIO

keydict = {}

'''
def my_callback(pinnum):  #回调函数，按键按下后，
    global keydict
    
    if GPIO.input(pinnum):
        keydict[pinnum] = 0
    else:
        keydict[pinnum] = 1
'''

def   daemonKey():
    global keydict
    while True:
        time.sleep(0.1)
        keys = keydict.keys()
        for i in keys:
            #print("i =  ",i)
            if GPIO.input(i):    #高电平，未按下
                keydict[i]  = 0
            else:
                keydict[i] += 1  #按下，每隔100ms计数值加1
        

def   initKey(pinnum):
    global keydict
    if pinnum in keydict:
        print('已初始化按键 ',pinnum)
    else:
        keydict[pinnum] = 0
        print('初始化按键 ',pinnum)
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pinnum,GPIO.IN, pull_up_down=GPIO.PUD_UP) #设为输入，上拉电阻
        #GPIO.RISING、GPIO.FALLING、GPIO.BOTH     ;bouncetime=200 去抖时间200ms
        #GPIO.add_event_detect(pinnum, GPIO.BOTH, callback = my_callback,bouncetime=200)
 
def   getKeySta(pinnum):
    return keydict.get(pinnum)
     
import  time
import  threading
 
if  __name__ == "__main__": 
    KEY_SUB = 13
    KEY_ADD = 5
    
    initKey(KEY_SUB)
    initKey(KEY_ADD)
    
    
    KeyThread = threading.Thread(target = daemonKey)     #创建多线程，启动接收任务
    KeyThread.start()    
    while True:
        time.sleep(1)
        print("KEY_SUB Value",getKeySta(KEY_SUB))
        print("KEY_ADD Value",getKeySta(KEY_ADD))

    
    #GPIO.remove_event_detect(KEY_SUB)
    #GPIO.remove_event_detect(KEY_ADD)


