import autopy3 as autopy
import time
import catchScreen
import getOffset
import getInfoFromScreen
import fiter
def homeTaskStart():
    autopy.mouse.move(397, 390)  # 平滑移动鼠标（上面那个是瞬间的）
    autopy.mouse.click()  # 单击
    times = 0
    while times < 10:
        # 移动街坊图标并点击
        fiter.moveAndClick(775, 182)
        # 移动祭坛图标并点击
        fiter.moveAndClick(420, 352)
        # 点击领取任务
        fiter.moveAndClick(205, 328)
        # 打开任务列表
        time.sleep(1)
        if(times==0):
            autopy.key.toggle('q', True, autopy.key.MOD_ALT)
            autopy.key.toggle('q', False, autopy.key.MOD_ALT)
        else:
            autopy.key.toggle('q', True, autopy.key.MOD_ALT)
            autopy.key.toggle('q', False, autopy.key.MOD_ALT)
            time.sleep(1)
            autopy.key.toggle('q', True, autopy.key.MOD_ALT)
            autopy.key.toggle('q', False, autopy.key.MOD_ALT)
        # 判断任务的类型
        catchScreen.catchAllScreen()
        time.sleep(1)
        while True:
            if(isinstance(getOffset.getOffsetValue("home\\xiaoyao"), list)):
                print("小妖")
                attr = getOffset.getOffsetValue("home\\xiaoyao")
                fiter.moveAndClick(attr[0] + 70, attr[1])
                isUser("xiaoyao", 70)
                break
            elif(isinstance(getOffset.getOffsetValue("home\\yuanding"), list)):
                print("园丁")
                attr = getOffset.getOffsetValue("home\\yuanding")
                fiter.moveAndClick(attr[0] + 65, attr[1])
                isUser("yuanding", 65)
                break
            elif(isinstance(getOffset.getOffsetValue("home\\gongshuban"), list)):
                print("公输般")
                attr = getOffset.getOffsetValue("home\\gongshuban")
                fiter.moveAndClick(attr[0] -45, attr[1])
                if(findNPC("gongshuban")):
                    print("haha")
                    fiter.moveAndClick(249,379)
                    fiter.moveAndClick(216,330)
                break
        # 点击回家
        fiter.moveAndClick(785, 551)
        times += 1

def isUser(classify,offset):
    time.sleep(1)
    catchScreen.catchScreen(337, 200, 555, 270, "home\\users")
    time.sleep(2)
    a = 1
    attr = getOffset.getOffsetValue("home\\" + classify)
    while True:
        if(a==1):
            if(findUser(555, 301, classify,attr, offset)):
                break
        elif(a==2):
            if(findUser(490,330, classify,attr, offset)):
                break
        elif(a==3):
            if(findUser(437,356, classify,attr, offset)):
                break
        elif(a==4):
            if(findUser(494,387, classify,attr, offset)):
                break
        elif(a==5):
            if(findUser(554,419, classify,attr, offset)):
                break
        elif(a==6):
            if(findUser(613,389, classify,attr, offset)):
                break
        elif(a==7):
            if(findUser(675,357, classify,attr, offset)):
                break
        elif(a==8):
            if(findUser(614,329, classify,attr, offset)):
                break
        a += 1
        if(a==9):
            a=1
def findUser(x,y,classify,attr,offset):
    a = False
    time.sleep(1)
    fiter.moveAndClick(x, y)
    time.sleep(1)
    fiter.moveAndClick(175, 328)
    fiter.moveAndClick(attr[0] + offset, attr[1])
    catchScreen.catchAllScreen()
    if (getOffset.getOffsetValue("home\\users") == "none"):
        findNPC(classify)
        a = True
    return a

def findNPC(classify):
    time.sleep(1)
    # 判断是否走到NPC面前
    x1 = ""
    while True:
        # 截取左上地图坐标
        catchScreen.catchScreen(40, 65, 140, 85, "position")
        time.sleep(1)
        position = getInfoFromScreen.getInfomation_nodeal("position")
        if (x1 == position):
            break
        else:
            x1 = position
    # 点击
    if(classify=="xiaoyao"):
        fiter.moveAndClick(202, 328)
        fiter.isFighting()
    elif(classify=="yuanding"):
        fiter.moveAndClick(210, 346)
    elif(classify=="gongshuban"):
        return True
homeTaskStart()