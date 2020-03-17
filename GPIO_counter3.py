import ctypes
import threading
import time
 
pluseer = ctypes.cdll.LoadLibrary('./GPIO_counter.so')

pluseer.initFrq(26)

thread_hi = threading.Thread(target=pluseer.threadCounter)
thread_hi.start()

while True:
    rotate = (int)((60 * pluseer.getFrq()) / (11 * 10))
    speed  = (int)(3.6 * (pluseer.getFrq() * 3.14 * 1.05) / (11 * 10))
    print("frq:",pluseer.getFrq(),rotate,speed)
    time.sleep(1)
    
