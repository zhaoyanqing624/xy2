from screenFilter import catchScreen, dealScreen, getInfoFromScreen
import getOffset
import time
import fiter
import random

def testx():
    while(True):
        time.sleep(5)
        catchScreen.catchScreen(40, 65, 1100, 585, "test")
        time.sleep(1)
        attr_start = getOffset.getOffsetValue_smallGhostStart()
        time.sleep(1)
        if(isinstance(attr_start,list)):
            # 点击确认
            print("一轮结束")
            time.sleep(2)
            fiter.moveAndClick(605+random.randint(0,5),490+random.randint(0,5))
            time.sleep(5)
            fiter.moveAndClick(852+random.randint(0,5),464+random.randint(0,5))
            time.sleep(2)
            fiter.moveAndClick(906 + random.randint(0, 5), 240 + random.randint(0, 5))
            time.sleep(1)
            fiter.moveAndClick(906 + random.randint(0, 5), 240 + random.randint(0, 5))

def bangpai_task():
    # catchScreen.catchScreen2(805, 205, 915, 240, "fight")
    while(True):
        time.sleep(2)
        fiter.moveAndClick(906 + random.randint(0, 5), 240 + random.randint(0, 5))
        time.sleep(2)
        catchScreen.catchScreen(40, 65, 1100, 800, "test")
        time.sleep(1)
        #attr1 = getOffset.getOffsetValue_my("bangpai2")
        attr2 = getOffset.getOffsetValue_my("bangpai2")
        for num in range(0,10):
            time.sleep(1)
            if(False):
                print("挑战帮主")
                break
            elif(isinstance(attr2,list)):
                print("交付药材")
                time.sleep(1)
                fiter.moveAndClick(attr2[0] + 20 + random.randint(0, 5), attr2[1] + 60 + random.randint(0, 5))
                break
            elif (isinstance(getOffset.getOffsetValue_my("bangpai3"), list)):
                print("药店购买")
                time.sleep(1)
                fiter.moveAndClick(802 + random.randint(0, 5), 625 + random.randint(0, 5))
                break
            elif (isinstance(getOffset.getOffsetValue_my("bangpai4"), list)):
                print("宣读公告")
                time.sleep(1)
                fiter.moveAndClick(854 + random.randint(0, 5), 683 + random.randint(0, 5))
                break



bangpai_task()


