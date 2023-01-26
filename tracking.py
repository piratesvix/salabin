import cv2
import mediapipe as mp
import time

target = cv2.VideoCapture(0)
mov = mp.solutions.hands
salabin = mov.Hands()

targetDraw = mp.solutions.drawing_utils


while True:
    success, frame = target.read()
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    res = salabin.process(frameRGB)
    
    if res.multi_hand_landmarks:
      for hand in res.multi_hand_landmarks:
        targetDraw.draw_landmarks(frame, hand, mov.HAND_CONNECTIONS)

    cv2.imshow("Image", frame)
    cv2.waitKey(1)

target.release()
cv2.destroyAllWindows()