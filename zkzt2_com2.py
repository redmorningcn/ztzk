'''
作者：redmorningcn   200312
描述：直流电机控制板ZK-ZT2上位机控制程序
包：Zkzt2Data，(self,port,baund = 9600)，
方法：setSpeed(self,speed,frq = 1000,direction = STA_CW):设置速度，其中speed 为%0-%100,可调速度。
'''
import ctypes
from   SerialPort import *

#Checker= ctypes.cdll.LoadLibrary(".\\CrcCheck.dll")
#不同的操作系统，打印对应的信息
if platform.system() == "Linux":
    Checker = CDLL("./CrcCheck.so")
    Frqer   = CDLL("./GPIO_counter.so")
else:
    Checker = CDLL(".\\CrcCheck.dll")
    Frqer   = CDLL(".\\GPIO_counter.dll")

STA_CW  = 0x00              #正转
STA_CCW = 0x01              #反转
STA_STOP= 0x02              #停止
STA_SD  = 0x03              #刹车

code =  0xe0
addr =  0x00

class Zkzt2_ST(ctypes.Structure):
    _fields_ = [("code",    ctypes.c_uint8),
                ("addr",    ctypes.c_uint8),
                ("status",   ctypes.c_uint8),
                ("speedH",  ctypes.c_uint8),
                ("speedL",  ctypes.c_uint8),
                ("frqH",   ctypes.c_uint8),
                ("frqL",   ctypes.c_uint8),
                ("bcc",     ctypes.c_uint8)
                ]


class Zkzt2Data:
    def __init__(self,port,baund = 9600):

        self.sendbuf = Zkzt2_ST(code,addr)      #定义发送结构体
        self.recvbuf = Zkzt2_ST()               #定义接收结构体

        self.ser     = SerialPort(port,baund)   #初始化串口
        self.ser.open()                         #打开串口

        #pcThread = threading.Thread(target = self.ser.recv)     #创建多线程，启动接收任务
        #pcThread.start()

    def stop(self):
        self.sendbuf.status = STA_STOP
        self.sendbuf.bcc = Checker.GetBccCheck(ctypes.byref(self.sendbuf),ctypes.sizeof(Zkzt2_ST)-1)
        
        print(self.sendbuf.status,self.sendbuf.bcc)
        self.ser.send(self.sendbuf)
    def setSpeed(self,speed,frq = 1000,direction = STA_CW):
        self.sendbuf.status = direction            #设置状态，默认正转
        self.sendbuf.speedH = 0x00
        self.sendbuf.speedL = speed
        print(frq,frq>>8,frq)
        self.sendbuf.frqH   = frq >> 8
        self.sendbuf.frqL   = frq
        
        self.sendbuf.bcc = Checker.GetBccCheck(ctypes.byref(self.sendbuf),ctypes.sizeof(Zkzt2_ST)-1)
        
        print(self.sendbuf.status,self.sendbuf.bcc)
        self.ser.send(self.sendbuf)



import  threading

def  taskSecond():
    while True:
        time.sleep(1)
        print("频率：",Frqer.getFrq())

if __name__=="__main__":
    #port    = "COM10"                  #平台不同，打开方式不同
    if platform.system() == "Linux":
        port = "/dev/ttyUSB0"
        #port = "/dev/ttyUSB1"
    else:
        port  = "COM10"

    pin     = 26
    
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
    #motor.stop()
    #sendData = Zkzt2_ST(0xE0,0x01,0x00,0x00,0x32,0x03,0x20,0xF0)
    #bcc = Checker.GetBccCheck(ctypes.byref(sendData),ctypes.sizeof(sendData)-1)
    #print(bcc)

