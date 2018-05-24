import autopy3 as autopy
import time
import getScreen
import getOffset
import fiter
from screenFilter import catchScreen
from screenFilter import dealScreen
import random
from monkey import dealScreenMonkey
def monkeyTaskStart():
    autopy.mouse.move(100, 20)  # 平滑移动鼠标（上面那个是瞬间的）
    autopy.mouse.click()  # 单击
    #(地图大小为120，100)
    for i in range(1, 60):
        while True:
            print("finding...")
            getScreen.window_capture("D:\\zhaoyq\\screen\\allScreen.png")
            dealScreenMonkey.dealMonkeyPicture()
            attr = getOffset.getOffsetValue_Monkey()
            print(attr)
            if(isinstance(attr, list)):
                autopy.mouse.move(attr[0]+200, attr[1]-50+200)
                autopy.mouse.click()  # 单击
                time.sleep(1)
                catchScreen.catchAllScreen()
                time.sleep(1)
                dealScreen.dealScreen("allScreen")
                if(isinstance(getOffset.getOffsetValue("monkey\\monkey_1"), list)):
                    break
                else:
                    fiter.isWalking()
        fiter.moveAndClick(310+random.randint(0,10), 343+random.randint(0,10))
        time.sleep(1)
        fiter.moveAndClick(228+random.randint(0,10),325+random.randint(0,10))
        fiter.isFight(i)
        time.sleep(1)
        # autopy.key.toggle('c', True, autopy.key.MOD_ALT)
        # autopy.key.toggle('c', False, autopy.key.MOD_ALT)
        fiter.moveAndClick(131+random.randint(0,10), 240+random.randint(0,10))
        fiter.isWalking()
        fiter.moveAndClick(290+random.randint(0,10), 365+random.randint(0,10))

monkeyTaskStart()