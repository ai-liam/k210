from PIL import Image
import cv2 as cv
import os

#from:https://blog.csdn.net/weixin_38632246/article/details/94393923
# https://blog.csdn.net/weixin_40446557/article/details/104059660

def png_to_jpg(png_file_path="./img/a/1.png"):
    try:
        img = cv.imread(png_file_path, 0)
        w, h = img.shape[::-1]
        infile = png_file_path
        outfile = os.path.splitext(infile)[0] + "_png.jpg"
        img = Image.open(infile)
        if len(img.split()) == 4:
            # prevent IOError: cannot write mode RGBA as BMP
            r, g, b, a = img.split()
            img = Image.merge("RGB", (r, g, b))
            img.convert('RGB').save(outfile, quality=80)
        else:
            img.convert('RGB').save(outfile, quality=80)
        os.remove(png_file_path)  # 是否删除
        print("ok:",png_file_path)
        return outfile
    except Exception as e:
        print("PNG转换JPG 错误file:", png_file_path)
        print("PNG转换JPG 错误:", e)

def convert_one(file_path = "./img/a/1.png"):
    if file_path.endswith('.png'):
        png_to_jpg(file_path)

def convert_dir(path="./img/a"):
    img_dir = os.listdir(path)
    for img in img_dir:
        if img.endswith('.png'):
            file_path = os.path.join(path,img) #path + img
            png_to_jpg(file_path)
    # img_dir = os.listdir(path)
    # for img in img_dir:
    #     print(img)
    print(f"[png to jpg :convert_dir {path} end]")

def convert_multiple_dir(root_dir="./img"):
    dir_list = list(
        filter(
            lambda x: not x.startswith(".")
                      and os.path.isdir(os.path.join(root_dir, x)),
            os.listdir(root_dir),
        )
    )
    for p in dir_list:
        # if (p == 'train' or p== 'val' or p == 'test'):
        #     print('is '+p)
        # else:
        path = os.path.join(root_dir, p)
        #print(path)
        convert_dir(path)
    print('[png to jpg :convert_multiple_dir end]')

if __name__ == "__main__":
    path ="/Users/liampro/Downloads/dataLake/images/图像分类/垃圾分类/DATASET_clean/temp"
    path1 =path+"/O"
    convert_dir(path= path1 )
    