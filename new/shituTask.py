import autopy3 as autopy
import time
from screenFilter import catchScreen
import getOffset
import fiter
from new import score as scoreShitu
def shituTaskStart():
    autopy.mouse.move(100, 20)  # 平滑移动鼠标（上面那个是瞬间的）
    autopy.mouse.click()  # 单击
    # # 地图寻路 东海渔村
    # time.sleep(1)
    # autopy.key.toggle('2', True, autopy.key.MOD_ALT)
    # autopy.key.toggle('2', False, autopy.key.MOD_ALT)
    # time.sleep(1)
    # fiter.moveAndClick_fast(658, 426)
    # fiter.moveAndClick_fast(290, 430)
    # fiter.isWalking()
    # autopy.key.toggle('2', True, autopy.key.MOD_ALT)
    # autopy.key.toggle('2', False, autopy.key.MOD_ALT)
    # autopy.key.toggle('1', True, autopy.key.MOD_ALT)
    # autopy.key.toggle('1', False, autopy.key.MOD_ALT)
    # autopy.key.toggle('5', True, autopy.key.MOD_ALT)
    # autopy.key.toggle('5', False, autopy.key.MOD_ALT)
    # # 计算师徒中介人位置
    # getScreen.window_capture("D:\\zhaoyq\\screen\\allScreen.png")
    # dealScreen.dealShituPicture()
    # attr = getOffset.getOffsetValue_Shitu()
    # autopy.mouse.move(attr[0] + 200, attr[1] - 50 + 200)
    # autopy.mouse.click()  # 单击
    # fiter.moveAndClick_fast(277, 434)
    # fiter.moveAndClick_fast(405, 255)
    # fiter.isWalking()
    # fiter.isFight()
    # time.sleep(1)
    # fiter.moveAndClick_fast(200, 333)
    # fiter.moveAndClick_fast(445, 237)
    # fiter.isWalking()
    # fiter.moveAndClick_fast(200, 328)
    # fiter.moveAndClick_fast(200, 328)
    # fiter.moveAndClick_fast(200, 328)
    # autopy.key.toggle('1', True, autopy.key.MOD_ALT)
    # autopy.key.toggle('1', False, autopy.key.MOD_ALT)
    # time.sleep(1)
    # 循环任务
    for i in range(1, 10):
        time.sleep(0.5)
        autopy.key.toggle('5', True, autopy.key.MOD_ALT)
        autopy.key.toggle('5', False, autopy.key.MOD_ALT)
        time.sleep(0.5)
        fiter.moveAndClick_fast(400, 315)
        fiter.moveAndClick_fast(400, 315)
        time.sleep(1)
        fiter.moveAndClick_fast(260, 345)
        time.sleep(1)
        autopy.key.toggle('q', True, autopy.key.MOD_ALT)
        autopy.key.toggle('q', False, autopy.key.MOD_ALT)
        time.sleep(1)
        # 点击任务名称
        catchScreen.catchAllScreen()
        time.sleep(1)
        attr = getOffset.getOffsetValue("shitu\\shitu_1")
        fiter.moveAndClick_fast(attr[0], attr[1] + 20)
        time.sleep(1)
        fiter.moveAndClick_fast(410, 255)
        fiter.isWalking()
        fiter.isFight()
        time.sleep(1)
        fiter.moveAndClick_fast(attr[0], attr[1] + 20)
        time.sleep(1)
        fiter.moveAndClick_fast(445, 237)
        fiter.isWalking()
        fiter.moveAndClick_fast(200, 328)
        time.sleep(1)
        autopy.key.toggle('1', True, autopy.key.MOD_ALT)
        autopy.key.toggle('1', False, autopy.key.MOD_ALT)
        time.sleep(0.5)
        # 判断是否关闭大话精灵
        catchScreen.catchAllScreen()
        time.sleep(1)
        if(isinstance(getOffset.getOffsetValue_Dahuajingling(), list)):
            time.sleep(0.5)
            fiter.moveAndClick_fast2(400, 172)
        # 判断是否打分
        scoreShitu.score()
        autopy.key.toggle('q', True, autopy.key.MOD_ALT)
        autopy.key.toggle('q', False, autopy.key.MOD_ALT)
        time.sleep(0.5)
        fiter.moveAndClick_fast(200, 328)
        time.sleep(0.5)
        fiter.moveAndClick_fast(200, 328)

shituTaskStart()
