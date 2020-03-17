'''
作者：redmonringcn  20.03.01
包：  SerialPort (包初始化：port,buand  端口，和波特率)
方法：open     (打开串口)
方法：close    (关闭串口)
方法：send     (发送数据：数据data,需配结束符)
方法：recv     (接收数据：任务需在线程执行;通过读取recv_len，
                判读是否有数据，数据存放在recv_buf，
                读取完recv_buf后，需清零recv_len值)
'''
import      serial
import      time
#import     threading
from        ctypes  import  *  
import      platform

#加载同目录下的dll
#

#不同的操作系统，打印对应的信息
if platform.system() == "Linux":
    Crc = CDLL("./CrcCheck.so")
else:
    Crc = CDLL(".\\CrcCheck.dll")
    
print(platform.system())

RECV_BUF_SIZE  =  1024     #接收缓冲区大小

class SerialPort:
    message=''
    def __init__(self,port,buand):
        super(SerialPort, self).__init__()
        try:
            self.ser=serial.Serial(port,buand)                  #配置串口
            self.ser.close()                                    #串口关闭
            if not self.ser.isOpen():
                self.ser.open()            
        except Exception as e:
            print("---串口打开异常---：", e)
        
    def open(self):                                             #方法，打开串口
        if not self.ser.isOpen():
            self.ser.open()
                
    def close(self):                                            #方法，关闭串口
        self.ser.close()
            
    def send(self,data):                                        #方法，发送数据
        #data = input("请输入要发送的数据（非中文）并同时接收数据: ")
        #n=self.port.write((data).encode())
        n=self.ser.write((data))
        return n


    def recv(self):                                             #方法，接收数据
            
        lst_num = 0                                             #前次接收到的数据长度
        self.recv_buf       = (c_byte * RECV_BUF_SIZE)()        #接收数据缓存区
        buflen              = RECV_BUF_SIZE - 1
        self.recv_len       = 0                                 #接收数据长度

        #print(sizeof(self.recv_buf))
        while True:
            if self.ser.in_waiting:                             #有数据
                if((self.ser.in_waiting > lst_num)):
                    lst_num = self.ser.in_waiting               #两次后，接收不增，才确认接收完成
                    time.sleep(0.005)                           #停5ms
                    #print("已接收：%d,%d",lst_num,self.ser.in_waiting,self.ser.in_waiting > lst_num)
                else:
                    #print("接收完成",lst_num,self.ser.in_waiting)
                    lst_num = 0                                 #准备下次接收
                    self.recv_len       = self.ser.in_waiting   #数据长度
                    if(self.ser.in_waiting > buflen):  
                        self.recv_len = buflen
                    self.recv_buf       = self.ser.read(self.recv_len ) #数据读取 

import threading

if __name__=='__main__':
    if platform.system() == "Linux":
        serialPort = "/dev/ttyUSB0"
    else:
        serialPort  = "COM8"                                    #串口

    baudRate    =  9600                                         #波特率
    
    mSerial  = SerialPort(serialPort,baudRate)
    mSerial1 = SerialPort(serialPort,baudRate)

    mSerial.open()
    t1=threading.Thread(target=mSerial.recv)

    send_buf = (c_uint8 * 5)(0x55,0xDD,0xFF,0x01,0xCE)
    crc_get = Crc.GetCheckSum(send_buf,sizeof(send_buf)-1)
    print(crc_get,send_buf[sizeof(send_buf)-1],crc_get == send_buf[sizeof(send_buf)-1])
    send_buf = (c_byte * 5)(0x31,0x31,0x31,0x31,0x31 )
    
    print(sizeof(send_buf))
    for i in range(len(send_buf)):
        print("send[%d] = %0X"%(i,send_buf[i]))

    #send_buf = "testing minicom\r\n"
    t1.start()
    while True:
        time.sleep(1)
        if(mSerial.recv_len):
            print(mSerial.recv_buf)
            crc_get = Crc.GetCheckSum(mSerial.recv_buf,mSerial.recv_len-1)
            print(crc_get,mSerial.recv_buf[mSerial.recv_len-1])
            #print(len(mSerial.recv_buf))
            #if(crc_get == mSerial.recv_buf[mSerial.recv_len-1]):
             #   print("校验成功！")
            #    mSerial.send_data(send_buf)
            mSerial.send(send_buf)
            print(send_buf)
            mSerial.recv_len = 0
        
        #mSerial.send_data()


