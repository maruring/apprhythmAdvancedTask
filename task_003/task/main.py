import cv2
import os
import glob
from PIL import Image
import shutil


# mediaディレクトリを中身を削除する
def delete_media_files():
    path = os.path.abspath('media')
    dirs = glob.glob(path + '/*')
    for dir in dirs:
        files = glob.glob(dir + '/*')
        for file in files:
            os.remove(file)
    print('写真を削除しました')


# 画像処理して返す
def pred():
    # 先頭の画像を選択
    image_path = glob.glob('media/before_image/*')[0]
    image_path = os.path.abspath(image_path)
    # 画像読み込み
    im = cv2.imread(image_path, cv2.IMREAD_COLOR)
    # リサイズ処理が
    origin_size = im.shape
    im = cv2.resize(im, dsize=(500,500))
    # グレースケールに変換
    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # 二値化 thresholdは二つの出力がある。1つ目はretval,2つ目は二値画像
    retval, thresh = cv2.threshold(im_gray, 50, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # 輪郭の抽出 出力は輪郭画像，輪郭，輪郭の階層情報です
    contour_image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    # 矩形領域を保存する辞書
    rectangle_list = []

    # 各輪郭に対する処理
    for i in range(0, len(contours)):
        area = cv2.contourArea(contours[i])

    #     小さい領域と大きすぎる領域を除外
        if area < 1e3 or 1e5 < area:
            continue

        if len(contours[i]) > 0:
            rect = contours[i]
            x,y,w,h = cv2.boundingRect(rect)
            position_list = [x,y,w,h]
            rectangle_list.append(position_list)

    for pos in rectangle_list:
        x,y,w,h = pos
        cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)

    #       矩形毎に画像を保存
    image_name = os.path.splitext(os.path.basename(image_path))[0] + '.jpg'
    abs_path = os.path.abspath('media/after_image')
    save_name = os.path.join(abs_path, image_name)
    im = cv2.resize(im, dsize=(origin_size[0], origin_size[1]))
    print(im.shape)
    cv2.imwrite(save_name, im)

# ファイル名の変更
def change_img_name():
    before_input_name = glob.glob('media/before_image/*')[0]
    before_output_name = glob.glob('media/after_image/*')[0]

    after_name = 'picture.jpg'
    after_input_name = os.path.join(os.path.abspath('media/before_image'), after_name)
    after_output_name = os.path.join(os.path.abspath('media/after_image'), after_name)

    os.rename(before_input_name, after_input_name)
    os.rename(before_output_name, after_output_name)

# 試し
def attempt():
    attmpt_file_path = [path for path in glob.glob('../media/*') if 'attempt' in path]
    if attmpt_file_path:
        print('前の画像が存在しました')
        for file in attmpt_file_path:
            os.remove(file)
        print('前の画像を削除しました')
    path = glob.glob('../media/before_image/*')[0]
    # 画像読み込み
    im = cv2.imread(path, cv2.IMREAD_COLOR)
    # グレースケールに変換
    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # 二値化 thresholdは二つの出力がある。1つ目はretval,2つ目は二値画像
    # retval, thresh = cv2.threshold(im_gray, 50, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    thresh = cv2.adaptiveThreshold(im_gray,255,cv2.CALIB_CB_ADAPTIVE_THRESH,cv2.THRESH_BINARY,11,2)
    contour_image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    cv2.imwrite('../media/attempt_thresh.jpg', thresh)
    cv2.imwrite('../media/attempt_contour_image.jpg', contour_image)
