import cv2
import os

# movieディレクトリにモザイクを入れる動画を入れてください
movie_path = 'movie/***.***(拡張子)'
edited_movie_path = 'edited_movie'
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt2.xml')
# モザイク加工後のファイル名を指定してください
output_file_name = '***.***(拡張子)'



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
    face_rects = face_cascade.detectMultiScale(img, minNeighbors=5)
    for x,y,w,h in face_rects:
        img = mosaic_area(img, x, y, w, h)
    if face_rects == () or w<100 or h<100:
        img=mosaic_area(img,0,0,640,480)
    return img


cap = cv2.VideoCapture(movie_path)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
size = (width, height)

fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
writer = cv2.VideoWriter(os.path.join(os.getcwd(), edited_movie_path, file_name), fmt, frame_rate, size)

i = 1
while True:
    print("Frame:{}".format(i))
    ret, img = cap.read()

    if ret == False:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    edit_img = face_mosaic(img=img)
    writer.write(edit_img)
    # cv2.imshow('Video', edit_img)
    i += 1

writer.release()
cap.release()
cv2.destroyAllWindows()

print('---end---')