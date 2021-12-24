import cv2
import os

movie_path = 'movie/seiya.MP4'
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')


#顔に白い枠をつける
def detect_face(img):
    face_img = img.copy()
    face_rects = face_cascade.detectMultiScale(face_img, scaleFactor=1.2, minNeighbors=5)
    for (x,y,w,h) in face_rects:
        cv2.rectangle(face_img, (x,y), (x+w, y+h), (255,255,255), 10)
    return face_img

def mosaic(img, ratio=0.05):
    #顔の画像を圧縮する
    small = cv2.resize(img, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    # 圧縮した画像を拡大する → モザイク処理になる
    big = cv2.resize(small, img.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)
    return big

# モザイクをつける範囲を確定
def mosaic_area(img,x,y,w,h,ratio=0.05):
    dst = img.copy()
    dst[y:y+h, x:x+w] = mosaic(dst[y:y+h, x:x+w], ratio)
    return dst

def face_mosaic(img):
    face_rects = face_cascade.detectMultiScale(img)
    for x,y,w,h in face_rects:
        img = mosaic_area(img, x, y, w, h)
    if face_rects == () or w<100 or h<100:
        img=mosaic_area(img,0,0,640,480)
    return img


cap = cv2.VideoCapture(movie_path)

i = 1
while True:
    print("Frame:{}".format(i))
    ret, img = cap.read()

    if ret == False:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    edit_img = face_mosaic(img=img)

    cv2.imshow('Video', edit_img)
    i += 1
cap.release()
cv2.destroyAllWindows()