#For Images

import cv2
from random import randrange

trained_faced_data = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

img = cv2.imread('images.png')
#img = cv2.imread('bsb.png')
#img = cv2.imread('download.png')

grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_coordinates = trained_faced_data.detectMultiScale(grayscale_img)

for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x + w, y + h),
                  (randrange(256), randrange(256), randrange(256)), 2)

#print(face_coordinates)

cv2.imshow('Face Detector Project', img)
cv2.waitKey()

print("Code Completed")
"""

#For Video

import cv2

trained_faced_data = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

webcam = cv2.VideoCapture(0)

while True:
    frame_read, frame = webcam.read()
    grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_faced_data.detectMultiScale(grayscale_frame)

    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Face Detector Project', frame)
    key = cv2.waitKey(1)

    if key == 81 or key == 113:
        break

webcam.release()
print("Code Completed")

"""