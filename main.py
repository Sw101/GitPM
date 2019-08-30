import cv2, dlib, sys # 영상 처리를 위한 OpenCV 와 dlib sys 라이브러리를 추가.
import numpy as np # 행렬 연산을 위한 numpy 모듈을 이용.



cap = cv2.VideoCapture(0) 


while True:
    ret, img = cap.read()
    if not ret:
        break
    ori = img.copy()
    cv2.imshow('img', img)
    cv2.waitKey(1)
