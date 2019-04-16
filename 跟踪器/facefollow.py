import numpy as np
import cv2

def Getface(image):
    # 创建 classifier 下面的路径根据你自身的实际情况来
    cvo = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cvo.load('F:/opencv/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')
    # 设定灰度 这个可以直接彩图都行 为了精度合适，先设置灰度
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 识别面部（核心代码）
    faces = cvo.detectMultiScale(
        gray,
        scaleFactor = 1.3,
        minNeighbors = 5,
        minSize = (30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
        )

    # 给识别的面部进行方框标记
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
cam = cv2.VideoCapture(0)

width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (width, height))

while(cam.isOpened()):
    # 读取帧摄像头
    ret, frame = cam.read()
    if ret == True:
        # 输出当前帧
        frame = Getface(frame)
        out.write(frame)
        cv2.imshow('My face camera', frame)
        # ascii键盘按Q退出程序
        if (cv2.waitKey(30) & 0xff) == ord('q'):
            break
    else:
        break
out.release()
cam.release()
cv2.destrovAllWindows()
