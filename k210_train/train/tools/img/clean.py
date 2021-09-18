import tensorflow as tf
import io
import os
import os.path
from PIL import Image

# https://blog.csdn.net/pursuit_zhangyu/article/details/80190707
# 训练时，发现图片报：
# UnidentifiedImageError: cannot identify image file <_io.BytesIO object at 0x7fd5003f54f0>

# find . -name '.DS_Store'
# find . -name '.DS_Store' -delete

# eg:目录 ./img/a/1.jpg

# 获取图片 高 宽
# get_info("./img/a/1.jpg")
def get_info(file_path="./img/a/1.jpg"):
    try:
        img = tf.io.gfile.GFile(file_path, 'rb')
        #img = tf.gfile.FastGFile('00001.jpg', 'rb')
        encoded_jpg = img.read()
        encoded_jpg_io = io.BytesIO(encoded_jpg)
        image = Image.open(encoded_jpg_io)
        width, height = image.size
        #print(height ,'--' ,width)
        return True ,width, height
    except (OSError, NameError):
        print('[OSError]:'+file_path)
        return False ,0,0
    #print('done')

# 删除 无效，太小的图片
#clean_dir("./img/a",True,[10,10])
def clean_dir(path="./img/a", remove_error_img= True,min_size=[5,5]):
    img_dir = os.listdir(path)
    for img in img_dir:
        file_path = os.path.join(path,img) #path + img
        if img.startswith("."):
            print("[remove .] :",file_path)
            os.remove(file_path)
            continue
        #if (img.endswith('.jpg') or img.endswith('.jpeg')) :
        r,w,h = get_info(file_path)
        if r == False and remove_error_img:
            os.remove(file_path)
            print(f'[clean_dir remove]: {file_path} ')
            continue
        if remove_error_img and (w < min_size[0] or h < min_size[1]):
            os.remove(file_path)
            print(f'[clean_dir remove size]: {file_path} ')
    print(f'[clean_dir: {path} end]')

# 2级目录处理
# clean_multiple_dir("./img", True,[10,10])
def clean_multiple_dir(root_dir="./img", remove_error_img= True,min_size=[10,10]):
    dir_list = list(
        filter(
            lambda x: not x.startswith(".")
                      and os.path.isdir(os.path.join(root_dir, x)),
            os.listdir(root_dir),
        )
    )
    for p in dir_list:
        path = os.path.join(root_dir, p)
        #print(path)
        clean_dir(path,remove_error_img,min_size)
    print("[clean_multiple_dir end]")

if __name__ == "__main__":
    path ="/Users/liampro/Downloads/dataLake/images/图像分类/垃圾分类/DATASET_clean/temp"
    path1 =path+"/O"
    clean_dir(path= path1 )