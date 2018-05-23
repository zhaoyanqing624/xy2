import pytesseract
from PIL import Image
def getInfomation_nodeal(addr):
    text = pytesseract.image_to_string(Image.open("D:\\zhaoyq\\screen\\"+addr+".png"), lang='chi_sim')
    return text
def getInfomation(addr):
    text = pytesseract.image_to_string(Image.open("D:\\zhaoyq\\screen\\"+addr+"1.png"), lang='chi_sim')
    return text

