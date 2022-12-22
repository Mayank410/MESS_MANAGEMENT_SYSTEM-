import cv2 
import os
cam= cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)

face_detector=cv2.CascadeClassifier("C:\\Users\\dell\\Documents\\face_detect\\haarcascades\\haarcascade_frontalface_default.xml")

face_id= input("\n enter user id end press Enter key")
print('\n [INFO] Intializing face capture. Look the camera and wait....')

count=0

while (True):
    ret, img= cam.read()
    # img= cv2.flip(img, -1)
    gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(img, 1.3, 5)

    for (x, y, w, h) in faces :
        cv2.rectangle(img, (x, y), (x+w, y+h) ,(255,0,0), 2)
        count+=1

        cv2.imwrite("dataset/user." + str(face_id) + '.' + str(count)+ ".jpg", gray[y: y+h, x:x+w])

        cv2.imshow('image', img)

    # k= cv2.waitkey(100) & 0xff
    # if k ==27 :
    #  break
    if count >=30 :
        break 
cam.release()





            


