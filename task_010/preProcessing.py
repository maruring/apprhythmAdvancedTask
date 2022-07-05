import glob
import os

bad_images_dirs = glob.glob("./Dataset/bad/*")
img_NO = 0

for dir in bad_images_dirs:
    dir_name = dir.split("\\")[1]
    imgs = glob.glob(dir + "/*")
    base_path = "./Dataset/bad"
    for img in imgs:
        dst_path = base_path + dir_name + str(img_NO) + ".png"
        os.rename(img, dst_path)
        img_NO += 1



