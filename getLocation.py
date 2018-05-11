# 获取鼠标的位置
import os,time
import pyautogui as pag
try:
    while True:
            x,y = pag.position() #返回鼠标的坐标
            posStr="Position:"+str(x).rjust(4)+','+str(y).rjust(4)
            print(posStr)
            time.sleep(0.2)
            os.system('cls')#清楚屏幕
except  KeyboardInterrupt:
    print("end")