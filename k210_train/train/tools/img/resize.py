from PIL import Image
import os.path
import cv2 as cv


# https://blog.csdn.net/atyzy/article/details/77905463
#https://www.cnblogs.com/shoufengwei/p/8526105.html
#提取目录下所有图片,更改尺寸后保存到另一目录

# 只伸缩图片
def resize(img_file="./a/1.jpg",out_dir="",size=[224,224]):
    try:
        print(img_file)
        img = Image.open(img_file)
        (width, height) = img.size
        save_name = os.path.join(out_dir,os.path.basename(img_file))
        if out_dir == "":
            save_name = img_file+"_resize.jpg"
        if width >= height : # 横图
            nh = size[1]
            nw = int(width * nh / height)
            img = img.resize((nw,nh), Image.ANTIALIAS)
            img.save(save_name, quality=60)
        else :# 
            nw = size[0]
            nh = int(nw*height / width)
            img = img.resize((nw,nh), Image.ANTIALIAS)
            img.save(save_name, quality=60)
        if out_dir == "":
            os.remove(img_file)  # 是否删除
    except Exception as e:
        print('[ERROR]:', img_file)
        print(e)

# 居中裁剪图片
def crop(img_file="1.jpg",out_dir="",size=[224,224]):
    try:
        img = Image.open(img_file)
        (width, height) = img.size
        save_name = os.path.join(out_dir,os.path.basename(img_file))
        if out_dir == "":
            fpath, fname = os.path.split(img_file)
            ex = os.path.splitext(fname)[1]
            _name = os.path.splitext(fname)[0]
            name = f"{_name}_crop{ex}"
            save_name = os.path.join(fpath,name) #img_file+"_crop.jpg"
        if width >= height : # 横图
            nh = size[1]
            nw = int(width * nh / height)
            img = img.resize((nw,nh), Image.ANTIALIAS)
            x1 = int((nw - size[0])*0.5)
            x2 = x1+ size[0]
            img_c = img.crop((x1,0,x2,nh))
            img_c.save(save_name , quality=60)
        else :# 
            nw = size[0]
            nh = int(nw*height / width)
            img = img.resize((nw,nh), Image.ANTIALIAS)
            y1 = int(( nh - size[1])*0.5)
            y2 = y1+ size[1]
            img_c = img.crop((0,y1,nw,y2))
            img_c.save(save_name , quality=60)
        if out_dir == "":
            os.remove(img_file)  # 是否删除
    except Exception as e:
        print('[ERROR]:', img_file)
        print(e)

def resize_dir(path="./img/a",outdir="", size=[224,224],is_crop= True):
    img_dir = os.listdir(path)
    for img in img_dir:
        file_path = os.path.join(path, img) #path + img
        #print("[resize_dir path]:",file_path)
        if (img.endswith('.jpg') or img.endswith('.jpeg')) :
            if is_crop:
                crop(file_path, outdir,size)
            else:
                resize(file_path, outdir,size)
    print(f"[resize_dir {file_path} end]")

def resize_multiple_dir(root_dir="img",outdir="", size=[224,224],is_crop= True):
    dir_list = list(
        filter(
            lambda x: not x.startswith(".")
                      and os.path.isdir(os.path.join(root_dir, x)),
            os.listdir(root_dir),
        )
    )
    for p in dir_list:
        path = os.path.join(root_dir, p)
        if outdir == "":
            path_out = ""
        else:
            path_out = os.path.join(outdir, p)
            if not os.path.exists(outdir):
                os.makedirs(outdir)
            if not os.path.exists(path_out):
                os.makedirs(path_out)
        #print(path)
        resize_dir(path,path_out,size,is_crop)
    print('[resize_multiple_dir end]')


if __name__ == "__main__":
    path ="/Users/liampro/Downloads/dataLake/images/图像分类/垃圾分类/DATASET_clean/temp"
    path1 =path+"/O"
    resize_dir(path= path1 )
