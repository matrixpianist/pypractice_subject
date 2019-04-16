import cv2
cam = cv2.VideoCapture(0)

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
        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            break
    else:
        break
out.release()
cam.release()
cv2.destrovAllWindows()
