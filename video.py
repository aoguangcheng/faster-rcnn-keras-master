from keras.layers import Input
from frcnn import FRCNN
from PIL import Image
import numpy as np
import cv2
import sys

import time
frcnn = FRCNN()

# 调用摄像头
#capture=cv2.VideoCapture(0)
#  视频处理
capture=cv2.VideoCapture(sys.argv[1])
#capture=cv2.VideoCapture("img/4.mp4")
#capture=cv2.VideoCapture("img/3.mp4")
fps = capture.get(cv2.CAP_PROP_FPS)#获取帧率(每秒播放几张图像）

size = (int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

fNUMS = capture.get(cv2.CAP_PROP_FRAME_COUNT) #获取帧数

#创建VideoWriter对象，用于写视频
videoWriter = cv2.VideoWriter(sys.argv[2] + sys.argv[3] + ".avi", cv2.VideoWriter_fourcc('I', '4','2','0'), int(fps/2), size) #文件大
#videoWriter = cv2.VideoWriter("road.avi", cv2.VideoWriter_fourcc('X', 'V','I','D'), int(fps),size)
zhen = 0
#fps = 0.0
while(True):
    type = 2
    zhen = zhen + 100
    #t1 = time.time()
    # 读取某一帧
    ref,frame=capture.read()
    # 格式转变，BGRtoRGB
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    # 转变成Image
    frame = Image.fromarray(np.uint8(frame))

    # 进行检测
    frame = np.array(frcnn.detect_image(frame,type,zhen))

    # RGBtoBGR满足opencv显示格式
    frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)

    #fps  = ( fps + (1./(time.time()-t1)) ) / 2
    print("fps= %.2f"%(fps/2))
    frame = cv2.putText(frame, "fps= %.2f"%(fps/2), (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
   
   # cv2.imshow("video",frame)
    c = cv2.waitKey(int(1000/int(fps)))  #延迟 # c= cv2.waitKey(30) & 0xff
    
    videoWriter.write(frame)

#cv2.waitKey()
#cv2.destroyAllWindows()
capture.release()