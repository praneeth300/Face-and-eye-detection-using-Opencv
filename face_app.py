
import cv2
print('Done')

face_cascade=cv2.CascadeClassifier('praneeth.xml')

#to capture the video from the webcame
cap=cv2.VideoCapture(0)

while True:
    _,img=cap.read()

    #convert in to grayscale

    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #detect the faces

    faces=face_cascade.detectMultiScale(gray,1.1,4)

    #Draw a rectangle around each face

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(50,50,4),4)

    #display
    cv2.imshow('img',img)

    #Stop if escape key is pressed
    k=cv2.waitKey(30) & 0xff
    if k==27:
        break
#Realase the video capture opject
cap.release()