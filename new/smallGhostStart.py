import autopy3 as autopy
import time
import random
import catchScreen
import getScreen
import getOffset
import getInfoFromScreen
import fiter
import dealScreen
from new import score as scoreShitu

x = 0
y = 0
def smallGhostStart():
    autopy.mouse.move(100, 20)  # 平滑移动鼠标（上面那个是瞬间的）
    autopy.mouse.click()  # 单击
    for i in range(1, 240):
        time.sleep(0.5)
        autopy.key.toggle('5', True, autopy.key.MOD_ALT)
        autopy.key.toggle('5', False, autopy.key.MOD_ALT)
        fiter.moveAndClick(388 + random.randint(0, 10), 336)
        catchScreen.catchAllScreen()
        time.sleep(1)
        attr = getOffset.getOffsetValue_smallGhostMove()
        if(attr=="none"):
            print("不需要移动")
            getScreen.window_capture("D:\\zhaoyq\\screen\\allScreen.png")
            dealScreen.dealPicture_NPC("smallGhost")
            attr2 = getOffset.getOffsetValue_NPC("smallGhost", "zhongkui2")
            if(attr2=="none"):
                global x
                global y
                print("在地府")
                fiter.moveAndClick2(350 + random.randint(0, 10), 350)
                fiter.isWalking()
                autopy.key.toggle('5', True, autopy.key.MOD_ALT)
                autopy.key.toggle('5', False, autopy.key.MOD_ALT)
                time.sleep(0.5)
                fiter.moveAndClick(388 + random.randint(0, 10), 336)
                time.sleep(0.5)
                getScreen.window_capture("D:\\zhaoyq\\screen\\allScreen.png")
                dealScreen.dealPicture_NPC("smallGhost")
                attr3 = getOffset.getOffsetValue_NPC("smallGhost", "zhongkui")
                while True:
                    if(attr3=="none"):
                        getScreen.window_capture("D:\\zhaoyq\\screen\\allScreen.png")
                        dealScreen.dealPicture_NPC("smallGhost")
                        attr33 = getOffset.getOffsetValue_NPC("smallGhost", "zhongkui")
                        if(isinstance(attr33,list)):
                            x = attr33[0] + random.randint(0, 5) + 200-20
                            y = attr33[1] + random.randint(-10, 10) + 200 - 50
                            fiter.moveAndClick(x, y)
                            break
                    else:
                        x = attr3[0] + random.randint(0, 5) + 200
                        y = attr3[1] + random.randint(-10, 10) + 200 - 50 + 10
                        break
                fiter.moveAndClick(x,y)
                while True:
                    print("是否点击钟馗成功")
                    time.sleep(0.5)
                    catchScreen.catchAllScreen()
                    attr_start = getOffset.getOffsetValue_smallGhostStart()
                    if(attr_start=="none"):
                        fiter.moveAndClick(x,y)
                        time.sleep(1)
                    else:
                        break
                time.sleep(0.5)
            else:
                print("不在地府")
                x = attr2[0] + random.randint(0, 5) + 200
                y = attr2[1] + random.randint(-10, 10) + 200 - 50+10
                fiter.moveAndClick(attr2[0] + random.randint(0, 5) +200, attr2[1] + random.randint(-10, 10) +200-50+10)
                time.sleep(1)
        else:
            print("需要移动")
            autopy.mouse.move(attr[0]+random.randint(-10,10), attr[1])
            autopy.mouse.click(autopy.mouse.RIGHT_BUTTON)
            fiter.isWalking()
            time.sleep(0.5)
            autopy.key.toggle('5', True, autopy.key.MOD_ALT)
            autopy.key.toggle('5', False, autopy.key.MOD_ALT)
            fiter.moveAndClick(388 + random.randint(0, 10), 336)
            time.sleep(0.5)
            fiter.moveAndClick(460 + random.randint(0, 5), 460 + random.randint(-10, 10))
            time.sleep(0.5)
        while True:
            print("是否点击开始任务")
            catchScreen.catchAllScreen()
            time.sleep(1)
            attr_start = getOffset.getOffsetValue_smallGhostStart()
            if(isinstance(attr_start, list)):
                fiter.moveAndClick(attr_start[0] + random.randint(-20, 20), attr_start[1])
                break
            time.sleep(1)
        time.sleep(1)
        fiter.moveAndClick(222+random.randint(0,5), 333+random.randint(0,10))
        time.sleep(1)
        xuncha()
        fiter.moveAndClick_fast2(222,222)
        time.sleep(1)
        fiter.moveAndClick(39+random.randint(0,10), 254)
        fiter.isWalking()
        fiter.moveAndClick(205+random.randint(-10,10), 357)
        fiter.isFight(i)
        # 判断是否关闭大话精灵
        catchScreen.catchAllScreen()
        time.sleep(1)
        if(isinstance(getOffset.getOffsetValue_Dahuajingling(), list)):
            time.sleep(0.5)
            fiter.moveAndClick_fast2(400, 172)
        # 关闭物品栏
        catchScreen.catchAllScreen()
        time.sleep(1)
        if(isinstance(getOffset.getOffsetValue_Wupinlan(), list)):
            time.sleep(0.5)
            fiter.moveAndClick_fast2(190+random.randint(-10,10), 121)
        # 领取礼盒
        catchScreen.catchAllScreen()
        time.sleep(1)
        if(isinstance(getOffset.getOffsetValue_Box(), list)):
            print("领取礼盒")
            time.sleep(0.5)
            attr5 = getOffset.getOffsetValue_Box()
            if(attr5[0]>900):
                time.sleep(1)
            else:
                fiter.moveAndClick(attr5[0]+random.randint(-10,10)+50, attr5[1]+50+random.randint(0,5))
                time.sleep(40)
        # 返回
        time.sleep(1)
        print("点击回程")
        catchScreen.catchAllScreen()
        time.sleep(1)
        if(isinstance(getOffset.taskRight(),list)):
            time.sleep(0.5)
            attr6 = getOffset.taskRight()
            fiter.moveAndClick(attr6[0] + random.randint(0, 10)+30, attr6[1]-60 + random.randint(0, 10))
        else:
            fiter.moveAndClick(800 + random.randint(0, 10), 530+random.randint(0, 10))
        time.sleep(1)
        i+=1

def xuncha():
    # 判断是否是巡视的鬼
    while True:
        print("是否巡视鬼")
        time.sleep(1)
        catchScreen.catchScreen(10, 220, 190, 260, "smallGhost\\1")
        time.sleep(1)
        if (getInfoFromScreen.getInfomation("smallGhost\\1").find("捉") == -1):
            print("巡查")
            time.sleep(1)
            catchScreen.catchScreen(40, 65, 140, 85, "position1")
            time.sleep(1)
            dealScreen.dealScreen("position1")
            time.sleep(1)
            print(getInfoFromScreen.getInfomation("position1"))
            if(getInfoFromScreen.getInfomation("position1").find("地府")!=-1):
                print("巡查在地府")
                while True:
                    getScreen.window_capture("D:\\zhaoyq\\screen\\allScreen.png")
                    dealScreen.dealPicture_NPC("smallGhost")
                    attr44 = getOffset.getOffsetValue_NPC("smallGhost", "zhongkui")
                    if (isinstance(attr44, list)):
                        fiter.moveAndClick(attr44[0] + random.randint(10, 20) + 200 + 20,
                                           attr44[1] + random.randint(0, 10) + 200 - 50)
                        break
            else:
                print("巡查在长安")
                while True:
                    getScreen.window_capture("D:\\zhaoyq\\screen\\allScreen.png")
                    dealScreen.dealPicture_NPC("smallGhost")
                    attr45 = getOffset.getOffsetValue_NPC("smallGhost", "zhongkui2")
                    if (isinstance(attr45, list)):
                        fiter.moveAndClick(attr45[0] + random.randint(10, 20) + 200 - 20,
                                           attr45[1] + random.randint(0, 10) + 200 - 50)
                        break
            getScreen.window_capture("D:\\zhaoyq\\screen\\allScreen.png")
            dealScreen.dealPicture_NPC("smallGhost")
            attr44 = getOffset.getOffsetValue_NPC("smallGhost", "zhongkui")
            fiter.moveAndClick(attr44[0] + random.randint(10, 20) + 200-20, attr44[1] + random.randint(0, 10) + 200 - 50)
            time.sleep(1)
            while True:
                catchScreen.catchAllScreen()
                attr_start = getOffset.getOffsetValue_smallGhostStart()
                if (isinstance(attr_start, list)):
                    fiter.moveAndClick(attr_start[0] + random.randint(-20, 20), attr_start[1])
                    fiter.moveAndClick(222 + random.randint(0, 5), 333 + random.randint(0, 10))
                break
            time.sleep(1)
        else:
            print("普通捉拿")
            break
smallGhostStart()