from PIL import Image
from PIL import ImageGrab
def catchAllScreen():
    im = ImageGrab.grab()
    im.save("D:\\zhaoyq\\screen\\allScreen.png")

def catchScreen():
    bbox = (376, 230, 377, 231)
    im = ImageGrab.grab(bbox)
    # im = im.resize((400, 200),Image.ANTIALIAS)
    im.show()
    im.save('D:\\zhaoyq\\train\\faction\\xuanchuan_3.png')

# bbox = (150, 290, 600, 400)
# im = ImageGrab.grab(bbox)
# # im = im.resize((400, 200),Image.ANTIALIAS)
# im.show()
# im.save('D:\\zhaoyq\\train\\faction\\answer_2.png')
