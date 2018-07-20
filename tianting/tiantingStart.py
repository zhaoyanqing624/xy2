import autopy3 as autopy
import time
import random
from screenFilter import catchScreen, dealScreen, getInfoFromScreen
import getScreen
import getOffset
import fiter
def tiantingStart():
    autopy.mouse.move(100, 20)  # 平滑移动鼠标（上面那个是瞬间的）
    autopy.mouse.click()  # 单击
    time.sleep(0.5)
    autopy.key.toggle('5', True, autopy.key.MOD_ALT)
    autopy.key.toggle('5', False, autopy.key.MOD_ALT)
    fiter.moveAndClick(388 + random.randint(0, 10), 336)
    time.sleep(0.5)
    getScreen.window_capture("D:\\zhaoyq\\screen\\allScreen.png")
    dealScreen.dealPicture_NPC("tianting")
    attr = getOffset.getOffsetValue_NPC("tianting", "lijing")
    x = attr[0] + random.randint(0, 5) + 200 - 20
    y = attr[1] + random.randint(-10, 10) + 200 - 50
    fiter.moveAndClick(x, y)
    for i in range(1, 240):
        fiter.moveAndClick(180+random.randint(-10,10), 400)
        # 第一只怪
        time.sleep(1)
        fiter.moveAndClick(110 + random.randint(-5, 5), 240)
        tianting(i)
        # 第二只怪
        time.sleep(1)
        fiter.moveAndClick(160 + random.randint(-5, 5), 240)
        tianting(i+1)
        # 第三只怪
        time.sleep(1)
        fiter.moveAndClick(50 + random.randint(-5, 5), 255)
        tianting(i+2)
        # 第四只怪
        time.sleep(1)
        fiter.moveAndClick(100 + random.randint(-5, 5), 255)
        tianting(i+3)
        # 返回
        time.sleep(1)
        fiter.moveAndClick(25 + random.randint(0, 5), 265+ random.randint(0, 5))
        time.sleep(1)
        fiter.isWalking()
        while True:
            time.sleep(1)
            catchScreen.catchAllScreen()
            time.sleep(1)
            if(isinstance(getOffset.getOffsetValue_tiantingStart1(), list)):
                break
def tianting(i):
    time.sleep(1)
    fiter.isWalking()
    while True:
        catchScreen.catchAllScreen()
        time.sleep(1)
        if (isinstance(getOffset.getOffsetValue_tiantingStart(), list)):
            fiter.moveAndClick(200 + random.randint(-20, 20), 355)
            break
    fiter.isFight(i)
    # 判断是否关闭大话精灵
    catchScreen.catchAllScreen()
    time.sleep(1)
    if (isinstance(getOffset.getOffsetValue_Dahuajingling(), list)):
        time.sleep(0.5)
        fiter.moveAndClick_fast2(400, 172)
    # 关闭物品栏
    catchScreen.catchAllScreen()
    time.sleep(1)
    if (isinstance(getOffset.getOffsetValue_Wupinlan(), list)):
        time.sleep(0.5)
        fiter.moveAndClick_fast2(190 + random.randint(-10, 10), 121)
    # 领取礼盒
    catchScreen.catchAllScreen()
    time.sleep(1)
    if (isinstance(getOffset.getOffsetValue_Box(), list)):
        print("领取礼盒")
        time.sleep(0.5)
        attr5 = getOffset.getOffsetValue_Box()
        if (attr5[0] > 900):
            time.sleep(1)
        else:
            fiter.moveAndClick(attr5[0] + random.randint(-10, 10) + 50, attr5[1] + 50 + random.randint(0, 5))
            time.sleep(1)
tiantingStart()