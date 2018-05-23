import autopy3 as autopy
import time
import catchScreen
import getOffset
import getInfoFromScreen
import dealScreen
import fiter
import random
# 左键快速点击
def moveAndClick_fast(x,y):
    time.sleep(0.5)
    autopy.mouse.move(x, y)
    time.sleep(0.5)
    autopy.mouse.click()  # 单击
# 右键快速点击
def moveAndClick_fast2(x,y):
    time.sleep(0.5)
    autopy.mouse.move(x, y)
    time.sleep(0.5)
    autopy.mouse.click(autopy.mouse.RIGHT_BUTTON)  # 单击
def moveAndClick(x,y):
    time.sleep(1)
    autopy.mouse.smooth_move(x, y)
    time.sleep(1)
    autopy.mouse.click()  # 单击
def moveAndClick2(x,y):
    time.sleep(1)
    autopy.mouse.smooth_move(x, y)
    time.sleep(1)
    autopy.mouse.click(autopy.mouse.RIGHT_BUTTON) # 单击
# 为街坊使用
def isFighting():
    time.sleep(1)
    x1 = ""
    while True:
        # 截取左上地图坐标
        catchScreen.catchScreen(40, 65, 140, 85, "position1")
        position = getInfoFromScreen.getInfomation_nodeal("position")
        position1 = getInfoFromScreen.getInfomation_nodeal("position1")
        if (position == position1):
            break

# 一般战斗判断
def isFight(i):
    if(i%4==1):
        time.sleep(1)
        fiter.moveAndClick(88 + random.randint(-10, 10), 42)
        autopy.key.toggle('8', True, autopy.key.MOD_ALT)
        autopy.key.toggle('8', False, autopy.key.MOD_ALT)
        time.sleep(1)
        fiter.moveAndClick(238 + random.randint(-10, 10), 42)
        autopy.key.toggle('8', True, autopy.key.MOD_ALT)
        autopy.key.toggle('8', False, autopy.key.MOD_ALT)
        time.sleep(1)
        fiter.moveAndClick(388 + random.randint(-10, 10), 42)
        autopy.key.toggle('8', True, autopy.key.MOD_ALT)
        autopy.key.toggle('8', False, autopy.key.MOD_ALT)
        time.sleep(1)
        fiter.moveAndClick(538 + random.randint(-10, 10), 42)
        autopy.key.toggle('8', True, autopy.key.MOD_ALT)
        autopy.key.toggle('8', False, autopy.key.MOD_ALT)
        time.sleep(1)
        fiter.moveAndClick(688 + random.randint(-10, 10), 42)
        autopy.key.toggle('8', True, autopy.key.MOD_ALT)
        autopy.key.toggle('8', False, autopy.key.MOD_ALT)
        time.sleep(1)
        fiter.moveAndClick(88 + random.randint(-10, 10), 42)
    time.sleep(1)
    x = True
    while True:
        catchScreen.catchAllScreen()
        if (isinstance(getOffset.getOffsetValue("zidong"), list)):
            x = True
        else:
            print("over")
            break
def isWalking():
    time.sleep(2)
    a = 0
    # 判断是否走到NPC面前
    while True:
        # 截取左上地图坐标
        time.sleep(2)
        if(a % 2)==0:
            catchScreen.catchScreen(30, 65, 140, 85, "position")
        else:
            catchScreen.catchScreen(30, 65, 140, 85, "position0")
        degree = dealScreen.similarPicture("position","position0")
        if (degree == 0):
            break
        a += 1
    print("走路结束")
def isAuto():
    time.sleep(1)
    autopy.mouse.move(200, 248)  # 平滑移动鼠标（上面那个是瞬间的）
    while True:
        catchScreen.catchAllScreen()
        if(isinstance(getOffset.getOffsetValue("new\\auto"), list)):
            autopy.mouse.click()  # 单击
        else:
            break
    print("动画结束")
