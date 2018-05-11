import autopy3 as autopy,PIL
import time
import catchScreen
import getInfoFromScreen
import getOffset
def home_mouse():
    # autopy.mouse.smooth_move(400, 350)  # 平滑移动鼠标（上面那个是瞬间的）
    autopy.mouse.move(189, 350)  # 平滑移动鼠标（上面那个是瞬间的）
    autopy.mouse.click()  # 单击
    autopy.mouse.toggle(True)  # 按下左键
    autopy.mouse.toggle(False)  # 松开左键
    # 打开地图
    time.sleep(1)
    autopy.key.toggle('2', True, autopy.key.MOD_ALT)
    autopy.key.toggle('2', False, autopy.key.MOD_ALT)
    # 点击长安子图
    time.sleep(2)
    autopy.mouse.smooth_move(510, 420)  # 平滑移动鼠标（上面那个是瞬间的）
    autopy.mouse.click()  # 单击
    # 移动超级管家
    time.sleep(2)
    autopy.mouse.smooth_move(325, 355)  # 地图坐标为164，129
    autopy.mouse.click()  # 单击
    # 判断是否走到管家面前
    x1 = ""
    while True:
        # 截取左上地图坐标
        catchScreen.catchScreen(40, 65, 140, 85, "position")
        position = getInfoFromScreen.getInfomation("position")
        if(x1 == position):
            break
        else:
            x1 = position
    # 关闭大地图和小地图
    autopy.key.toggle('2', True, autopy.key.MOD_ALT)
    autopy.key.toggle('2', False, autopy.key.MOD_ALT)
    autopy.key.toggle('1', True, autopy.key.MOD_ALT)
    autopy.key.toggle('1', False, autopy.key.MOD_ALT)
    autopy.key.toggle('5', True, autopy.key.MOD_ALT)
    autopy.key.toggle('5', False, autopy.key.MOD_ALT)
    # 计算‘超级管家偏移量’ 再点击超级管家
    autopy.mouse.click()  # 单击
    time.sleep(2)
    autopy.mouse.smooth_move(225, 300)
    time.sleep(1)
    catchScreen.catchAllScreen()
    attr = getOffset.getOffsetValue("home\\home_start")
    autopy.mouse.smooth_move(attr[0]+32, attr[1]+217)
    time.sleep(1)
    autopy.mouse.click()  # 单击
    time.sleep(1)
    autopy.mouse.smooth_move(220, 346)
    time.sleep(1)
    autopy.mouse.click()  # 单击

home_mouse()