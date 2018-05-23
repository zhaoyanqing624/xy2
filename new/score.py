import getOffset
from screenFilter import catchScreen
import fiter
import time
def score():
    time.sleep(0.5)
    catchScreen.catchAllScreen()
    if(isinstance(getOffset.getOffsetValue("shitu\\score"), list)):
        fiter.moveAndClick_fast(228, 264)
        time.sleep(1)
        fiter.moveAndClick_fast(418, 505)
        fiter.moveAndClick_fast(418, 505)
