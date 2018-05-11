import autopy3 as autopy
import time
import random
import catchScreen
import getScreen
import getOffset
import getInfoFromScreen
import fiter
from monkey import dealScreenMonkey
def monkeyTaskStart():
    autopy.mouse.move(100, 20)  # 平滑移动鼠标（上面那个是瞬间的）
    autopy.mouse.click()  # 单击
    #(地图大小为120，100)
    while True:
        print("finding...")
        getScreen.window_capture("D:\\zhaoyq\\screen\\allScreen.png")
        dealScreenMonkey.dealMonkeyPicture()
        attr = getOffset.getOffsetValue_Monkey()
        print(attr)
        autopy.mouse.move(attr[0]+200, attr[1]-50+200)
        autopy.mouse.click()  # 单击
        if(isinstance(getOffset.getOffsetValue("monkey\\monkey_1"), list)):
            break
        else:
            fiter.isWalking()
    fiter.moveAndClick(310, 343)
    time.sleep(1)
    fiter.moveAndClick(228,325)
    fiter.isFight()
    time.sleep(1)
    autopy.key.toggle('c', True, autopy.key.MOD_ALT)
    autopy.key.toggle('c', False, autopy.key.MOD_ALT)
    fiter.moveAndClick(131, 240)
    fiter.isWalking()
    fiter.moveAndClick(290, 365)

monkeyTaskStart()