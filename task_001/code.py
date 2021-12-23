import cv2
import os
print(os.getcwd())

movie_path = 'movie/seiya.MP4'
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(movie_path)

def detect_face(img):
    face_img = img.copy()
    face_rects = face_cascade.detectMultiScale(face_img, scaleFactor=1.2, minNeighbors=1)
    for (x,y,w,h) in face_rects:
        cv2.rectangle(face_img, (x,y), (x+w, y+h), (255,255,255), 10)
    return face_img

i = 1
while True:
    print("Frame:{}".format(i))
    ret, img = cap.read()

    if ret == False:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    edit_img = detect_face(img=img)

    cv2.imshow('Video', edit_img)
    i += 1
cap.release()
cv2.destroyAllWindows()