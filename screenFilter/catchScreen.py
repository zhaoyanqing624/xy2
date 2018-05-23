
from PIL import ImageGrab
from screenFilter import dealScreen
import time
def catchAllScreen():
    time.sleep(1)
    im = ImageGrab.grab()
    im.save("D:\\zhaoyq\\screen\\allScreen.png")

def catchScreen(x,y,w,h,addr):
    bbox = (x, y, w, h)
    im = ImageGrab.grab(bbox)
    im.save("D:\\zhaoyq\\screen\\"+addr+".png")
    dealScreen.dealScreen(addr)
def catchScreenTest(x,y,w,h):
    bbox = (x, y, w, h)
    im = ImageGrab.grab(bbox)
    im.show()
    im.save("D:\\zhaoyq\\screen\\test.png")
# bbox = (150, 290, 600, 400)
# im = ImageGrab.grab(bbox)
# # im = im.resize((400, 200),Image.ANTIALIAS)
# im.show()
# im.save('D:\\zhaoyq\\train\\faction\\answer_2.png')
catchAllScreen()