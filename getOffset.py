
import cv2
import aircv as ac
# imgsr=cv2.imread("D:\\zhaoyq\\screen\\allScreen.png")
# imgtm=cv2.imread("D:\\zhaoyq\\screen\\chaojiguanjia.png")
# #获取模板图片的高和宽
# imgtmh1 = imgtm.shape[0]
# imgtmw1 = imgtm.shape[1]
# #与模版比对
# res=cv2.matchTemplate(imgsr,imgtm,cv2.TM_CCOEFF_NORMED)
# min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)
# img=cv2.rectangle(imgsr,max_loc,(max_loc[0]+imgtmw1,max_loc[1]+imgtmh1),(0,0,255),2)
# cv2.imshow('Image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
def getOffsetValue(npc):
    imsrc = ac.imread('D:\\zhaoyq\\screen\\allScreen.png')
    imobj = ac.imread("D:\\zhaoyq\\screen\\"+npc+".png")
    # find the match position
    pos = ac.find_template(imsrc, imobj)
    if pos is None:
        return "none"
    elif pos:
        circle_center_pos = list(pos['result'])
        x = int(circle_center_pos[0])
        y = int(circle_center_pos[1])
        attr = [x, y]
        return attr
    else:
        return "null"

def getOffsetValue_Monkey():
    imsrc = ac.imread('D:\\zhaoyq\\screen\\monkey\\allScreen.png')
    imobj = ac.imread("D:\\zhaoyq\\screen\\monkey\\monkey.png")
    # find the match position
    pos = ac.find_template(imsrc, imobj)
    if pos is None:
        return "none"
    elif pos:
        circle_center_pos = list(pos['result'])
        x = int(circle_center_pos[0])
        y = int(circle_center_pos[1])
        attr = [x, y]
        return attr
    else:
        return "null"
def getOffsetValue_Shitu():
    imsrc = ac.imread('D:\\zhaoyq\\screen\\shitu\\allScreen.png')
    imobj = ac.imread("D:\\zhaoyq\\screen\\shitu\\shitu.png")
    # find the match position
    pos = ac.find_template(imsrc, imobj)
    if pos is None:
        return "none"
    elif pos:
        circle_center_pos = list(pos['result'])
        x = int(circle_center_pos[0])
        y = int(circle_center_pos[1])
        attr = [x, y]
        return attr
    else:
        return "null"
def getOffsetValue_Dahuajingling():
    imsrc = ac.imread("D:\\zhaoyq\\screen\\allScreen.png")
    imobj = ac.imread("D:\\zhaoyq\\screen\\dahuajingling.png")
    # find the match position
    pos = ac.find_template(imsrc, imobj)
    if pos is None:
        return "none"
    elif pos:
        circle_center_pos = list(pos['result'])
        x = int(circle_center_pos[0])
        y = int(circle_center_pos[1])
        attr = [x, y]
        return attr
    else:
        return "null"
def getOffsetValue_Wupinlan():
    imsrc = ac.imread("D:\\zhaoyq\\screen\\allScreen.png")
    imobj = ac.imread("D:\\zhaoyq\\screen\\smallGhost\\wupin.png")
    # find the match position
    pos = ac.find_template(imsrc, imobj)
    if pos is None:
        return "none"
    elif pos:
        circle_center_pos = list(pos['result'])
        x = int(circle_center_pos[0])
        y = int(circle_center_pos[1])
        attr = [x, y]
        return attr
    else:
        return "null"
def getOffsetValue_Box():
    imsrc = ac.imread("D:\\zhaoyq\\screen\\allScreen.png")
    imobj = ac.imread("D:\\zhaoyq\\screen\\box.png")
    # find the match position
    pos = ac.find_template(imsrc, imobj)
    if pos is None:
        return "none"
    elif pos:
        circle_center_pos = list(pos['result'])
        x = int(circle_center_pos[0])
        y = int(circle_center_pos[1])
        attr = [x, y]
        return attr
    else:
        return "null"
def getOffsetValue_smallGhostMove():
    imsrc = ac.imread("D:\\zhaoyq\\screen\\allScreen.png")
    imobj = ac.imread("D:\\zhaoyq\\screen\\smallGhost\\smallGhost_1.png")
    # find the match position
    pos = ac.find_template(imsrc, imobj)
    if pos is None:
        return "none"
    elif pos:
        circle_center_pos = list(pos['result'])
        x = int(circle_center_pos[0])
        y = int(circle_center_pos[1])
        attr = [x, y]
        return attr
    else:
        return "null"
def getOffsetValue_smallGhostStart():
    imsrc = ac.imread("D:\\zhaoyq\\screen\\allScreen.png")
    imobj = ac.imread("D:\\zhaoyq\\screen\\smallGhost\\start.png")
    # find the match position
    pos = ac.find_template(imsrc, imobj)
    if pos is None:
        return "none"
    elif pos:
        circle_center_pos = list(pos['result'])
        x = int(circle_center_pos[0])
        y = int(circle_center_pos[1])
        attr = [x, y]
        return attr
    else:
        return "null"
def getOffsetValue_NPC(attr,attr2):
    imsrc = ac.imread("D:\\zhaoyq\\screen\\"+attr+"\\allScreen.png")
    imobj = ac.imread("D:\\zhaoyq\\screen\\"+attr+"\\"+attr2+".png")
    # find the match position
    pos = ac.find_template(imsrc, imobj)
    if pos is None:
        return "none"
    elif pos:
        circle_center_pos = list(pos['result'])
        x = int(circle_center_pos[0])
        y = int(circle_center_pos[1])
        attr = [x, y]
        return attr
    else:
        return "null"

def taskReturn(name):
    imsrc = ac.imread("D:\\zhaoyq\\screen\\allScreen.png")
    imobj = ac.imread("D:\\zhaoyq\\screen\\"+name+"\\"+"return.png")
    # find the match position
    pos = ac.find_template(imsrc, imobj)
    if pos is None:
        return "none"
    elif pos:
        circle_center_pos = list(pos['result'])
        x = int(circle_center_pos[0])
        y = int(circle_center_pos[1])
        attr = [x, y]
        return attr
    else:
        return "null"
def taskRight():
    imsrc = ac.imread("D:\\zhaoyq\\screen\\allScreen.png")
    imobj = ac.imread("D:\\zhaoyq\\screen\\"+"right.png")
    # find the match position
    pos = ac.find_template(imsrc, imobj)
    if pos is None:
        return "none"
    elif pos:
        circle_center_pos = list(pos['result'])
        x = int(circle_center_pos[0])
        y = int(circle_center_pos[1])
        attr = [x, y]
        return attr
    else:
        return "null"
def isLocation(attr1,attr2):
    imsrc = ac.imread("D:\\zhaoyq\\screen\\allScreen.png")
    imobj = ac.imread("D:\\zhaoyq\\screen\\"+"right.png")
    # find the match position
    pos = ac.find_template(imsrc, imobj)
    if pos is None:
        return "none"
    elif pos:
        circle_center_pos = list(pos['result'])
        x = int(circle_center_pos[0])
        y = int(circle_center_pos[1])
        attr = [x, y]
        return attr
    else:
        return "null"
