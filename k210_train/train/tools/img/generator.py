from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image

import os
import random

# 数据增强
"""
使用 ImageDataGenerator 来设置数据增强
* rotation_range 是角度值(在 0~180 范围内)，表示图像随机旋转的角度范围。
* width_shift 和 height_shift 是图像在水平或垂直方向上平移的范围(相对于总宽
度或总高度的比例)。
* shear_range 是随机错切变换的角度。
* zoom_range 是图像随机缩放的范围。
* horizontal_flip 是随机将一半图像水平翻转。如果没有水平不对称的假设(比如真
实世界的图像)，这种做法是有意义的。
* fill_mode 是用于填充新创建像素的方法，这些新像素可能来自于旋转或宽度 / 高度平移。 我们来看一下增强后的图像
"""

datagen = ImageDataGenerator(
        rotation_range=10,
        width_shift_range=0.1,
        height_shift_range=0.1,
        shear_range=0.1,
        zoom_range=0.1,
        horizontal_flip=False,
        fill_mode='nearest')

def generator_one(img_path="img/a/1.jpg",num=1):
    try:
        img = image.load_img(img_path, target_size=(224, 224))
        x = image.img_to_array(img)
        x = x.reshape((1,) + x.shape)
        num = num -1
        ran = random.randint(0,99)
        # 绘制9张随机增强后的图像
        for i, batch in enumerate(datagen.flow(x, batch_size=1)):
            draw=image.array_to_img(batch[0])
            fpath, fname = os.path.split(img_path)
            ex = os.path.splitext(fname)[1]
            _name = os.path.splitext(fname)[0]
            name = f"aug_{str(ran)}-{str(i)}-{_name}{ex}"
            save_path = os.path.join(fpath,name)
            draw.save(save_path)
            #print(save_path)
            if i == num:
                break
        #print('[generator ok]:',img_path)
    except Exception as e:
        print('error:', img_path)
        print(e)

def generator_dir(path="img/a",num=9):
    img_dir = os.listdir(path)
    for img in img_dir:
        file_path = os.path.join(path, img)
        #print("path",file_path)
        if img.startswith('aug_'):
            #print('had aug :',file_path)
            continue
        if (img.endswith('.jpg') or img.endswith('.jpeg') or img.endswith('.png') or img.endswith('.PNG') ) :
            generator_one(file_path, num)
    print(f"[generator_dir {path} end]")

def generator_multiple_dir(root_dir="img",num=9):
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
        generator_dir(path,num)
    print('[generator_multiple_dir end]')


if __name__ == "__main__":
    path ="/Users/liampro/Downloads/dataLake/images/图像分类/垃圾分类/DATASET_clean/temp"
    path1 =path+"/O"
    generator_dir(path= path1,num=4)
