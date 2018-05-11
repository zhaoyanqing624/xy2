import autopy3 as autopy,PIL
import time
import  catchScreen
import fiter
import getInfoFromScreen
import getOffset
# 545 285 （0，+10）
# autopy.mouse.move(352+5, 412+10)

#312 118
# time.sleep(1)
# autopy.mouse.move(554, 417)

# 判断任务的类型
# catchScreen.catchAllScreen()
# while True:
#     if (isinstance(getOffset.getOffsetValue("home\\xiaoyao"), list)):
#         attr = getOffset.getOffsetValue("home\\xiaoyao")
#         print("1")
#         print(attr)
#         break
#     elif (isinstance(getOffset.getOffsetValue("home\\yuanding"), list)):
#         print("2")
#         break
#     elif (isinstance(getOffset.getOffsetValue("home\\gongshuban"), list)):
#         print("3")
#         break
def findNPC(classify):
    time.sleep(1)
    # 判断是否走到NPC面前
    x1 = ""
    while True:
        # 截取左上地图坐标
        catchScreen.catchScreen(40, 65, 140, 85, "position")
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

print(findNPC("gongshuban"))