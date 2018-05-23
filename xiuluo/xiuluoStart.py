import autopy3 as autopy
import time
import random
import catchScreen
import getScreen
import getOffset
import getInfoFromScreen
import fiter
import dealScreen
def xiuluoStart():
    autopy.mouse.move(100, 20)  # 平滑移动鼠标（上面那个是瞬间的）
    autopy.mouse.click()  # 单击
    # (地图大小为120，100)
    getScreen.window_capture("D:\\zhaoyq\\screen\\allScreen.png")
    dealScreen.dealXiuluoPicture()
    attr = getOffset.getOffsetValue_NPC("xiuluo", "xiuluo")
    print(attr)
    autopy.mouse.move(attr[0] + 200, attr[1] - 50 + 200)
    # autopy.mouse.click()  # 单击

    getScreen.window_capture("D")

