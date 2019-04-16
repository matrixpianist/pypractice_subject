import cv2

face_patterns = cv2.CascadeClassifier('F:/opencv/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')

sample_image = cv2.imread("F:\身份证文件\mine\1寸蓝底.jpg")

faces = face_patterns.detectMultiScale(sample_image,scaleFactor=1.1,minNeighbors=5,minSize=(100, 100))

for (x, y, w, h) in faces:
    cv2.rectangle(sample_image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imwrite("F:\身份证文件\mine\1寸蓝底.jpg", sample_image)
