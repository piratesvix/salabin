import cv2
import mediapipe as mp
import time

target = cv2.VideoCapture(0)
mov = mp.solutions.hands
salabin = mov.Hands()


while True:
    success, frame = target.read()
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    res = salabin.process(frameRGB)
    print(res)

    cv2.imshow("Image", frame)
    cv2.waitKey(1)

target.release()
cv2.destroyAllWindows()