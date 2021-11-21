from keras.layers import Input
from frcnn import FRCNN 
from PIL import Image
import cv2
import glob,os
import sys

frcnn = FRCNN()

# 批量测试

ind = 0
zhen = 0
#while True:
dir1=sys.argv[1]
list1=dir1+'//*.jpg'
for img in glob.glob(list1):
    type = 1
    zhen = zhen + 1
    filepath,filename = os.path.split(img)

    ind=ind+1
    print(ind)
    save_path='C:\\Users\\AoGua\\IdeaProjects\\imagesClassA\\'+filename

    print(save_path)

    #img = input('Input image filename:')
    #try:
    image = Image.open(img)
    #except:
    #    print('Open Error! Try again!')
     #   continue
   # else:
    r_image = frcnn.detect_image(image,type,zhen)
   # r_image.show()
   # save_path='D:\\faster-rcnn-keras-master\\outimg\\'+str(ind)+'.jpg'
       # 第几张图片
    #print(ind)
  #  ind=ind+1
    
    r_image.save(save_path)
    
frcnn.close_session()
    