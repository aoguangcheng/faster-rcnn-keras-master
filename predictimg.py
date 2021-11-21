from keras.layers import Input
from frcnn import FRCNN
from PIL import Image
import sys
frcnn = FRCNN()

#  单图测试
zhen = 0
while True:
    type = 1
    zhen = zhen + 1
    #img = input('Input image filename:')
    img = sys.argv[1]
    try:
        image = Image.open(img)
    except:
        print('Open Error! Try again!')
        continue
    else:
        r_image = frcnn.detect_image(image,type,zhen)
        #r_image.show()
        r_image.save(sys.argv[2])
        break
frcnn.close_session()
