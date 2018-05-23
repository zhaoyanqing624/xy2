from PIL import Image
import cv2
import numpy as np
from PIL import ImageEnhance
def dealScreen_Nodeal(addr):
    image = Image.open("D:\\zhaoyq\\screen\\"+addr+".png").convert('L')
    # 亮度增强
    enh_bri = ImageEnhance.Brightness(image)
    brightness = 1.5
    image_brightened = enh_bri.enhance(brightness)
    # 色度增强
    enh_col = ImageEnhance.Color(image)
    color = 1.5
    image_colored = enh_col.enhance(color)
    # 对比度增强
    enh_con = ImageEnhance.Contrast(image)
    contrast = 1.5
    image_contrasted = enh_con.enhance(contrast)
    # 锐度增强
    enh_sha = ImageEnhance.Sharpness(image)
    sharpness = 3.0
    image_sharped = enh_sha.enhance(sharpness)
    image.save("D:\\zhaoyq\\screen\\"+addr+"1.png")
def dealScreen(addr):
    image = Image.open("D:\\zhaoyq\\screen\\"+addr+".png").convert('L')
    # 亮度增强
    enh_bri = ImageEnhance.Brightness(image)
    brightness = 1.5
    image_brightened = enh_bri.enhance(brightness)
    # 色度增强
    enh_col = ImageEnhance.Color(image)
    color = 1.5
    image_colored = enh_col.enhance(color)
    # 对比度增强
    enh_con = ImageEnhance.Contrast(image)
    contrast = 1.5
    image_contrasted = enh_con.enhance(contrast)
    # 锐度增强
    enh_sha = ImageEnhance.Sharpness(image)
    sharpness = 3.0
    image_sharped = enh_sha.enhance(sharpness)
    image.resize((300, 80), Image.ANTIALIAS).save("D:\\zhaoyq\\screen\\"+addr+"1.png", quality=95, dpi=(72, 72))
    # image.save("D:\\zhaoyq\\screen\\test1.png")
# 计算图片的相似度
def similarPicture(attr1,attr2):
    img1 = cv2.imread("D:\\zhaoyq\\screen\\"+attr1+".png")
    img2 = cv2.imread("D:\\zhaoyq\\screen\\"+attr2+".png")
    return classify_pHash(img1,img2)
# 平均哈希算法计算
def classify_pHash(image1,image2):
    image1 = cv2.resize(image1,(32,32))
    image2 = cv2.resize(image2,(32,32))
    gray1 = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)
    # 将灰度图转为浮点型，再进行dct变换
    dct1 = cv2.dct(np.float32(gray1))
    dct2 = cv2.dct(np.float32(gray2))
    # 取左上角的8*8，这些代表图片的最低频率
    # 这个操作等价于c++中利用opencv实现的掩码操作
    # 在python中进行掩码操作，可以直接这样取出图像矩阵的某一部分
    dct1_roi = dct1[0:8,0:8]
    dct2_roi = dct2[0:8,0:8]
    hash1 = getHash(dct1_roi)
    hash2 = getHash(dct2_roi)
    return Hamming_distance(hash1,hash2)
# 输入灰度图，返回hash
def getHash(image):
    avreage = np.mean(image)
    hash = []
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i,j] > avreage:
                hash.append(1)
            else:
                hash.append(0)
    return hash
# 计算汉明距离
def Hamming_distance(hash1,hash2):
    num = 0
    for index in range(len(hash1)):
        if hash1[index] != hash2[index]:
            num += 1
    return num
# 计算师徒中介人
def dealShituPicture():
    img=cv2.imread('D:\\zhaoyq\\screen\\allScreen.png',cv2.IMREAD_COLOR)
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower_blue = np.array([0, 60, 10])
    upper_blue = np.array([50, 255, 255])
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    res=cv2.bitwise_and(img,img,mask=mask)
    cv2.imwrite('D:\\zhaoyq\\screen\\shitu\\allScreen.png',res, [int(cv2.IMWRITE_PNG_COMPRESSION), 1])
# 计算修罗NPC
def dealXiuluoPicture():
    img=cv2.imread('D:\\zhaoyq\\screen\\allScreen.png',cv2.IMREAD_COLOR)
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower_blue = np.array([0, 60, 10])
    upper_blue = np.array([50, 255, 255])
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    res=cv2.bitwise_and(img,img,mask=mask)
    cv2.imwrite('D:\\zhaoyq\\screen\\xiuluo\\allScreen.png',res, [int(cv2.IMWRITE_PNG_COMPRESSION), 1])

def dealPicture_NPC(addr):
    img=cv2.imread('D:\\zhaoyq\\screen\\allScreen.png',cv2.IMREAD_COLOR)
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower_blue = np.array([0, 60, 10])
    upper_blue = np.array([50, 255, 255])
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    res=cv2.bitwise_and(img,img,mask=mask)
    cv2.imwrite("D:\\zhaoyq\\screen\\"+addr+"\\allScreen.png",res, [int(cv2.IMWRITE_PNG_COMPRESSION), 1])
