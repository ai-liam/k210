
import os, random, shutil

def copy_file(file_dir,tar_dir,num=40,pre="",i=0,step =2):
    path_dir = os.listdir(file_dir)# get all file['126.jpg', '221.jpg','234.jpg']
    _max= len(path_dir)
    if num > _max:
        num = _max
    sample = random.sample(path_dir, num)# get random file['126.jpg', '221.jpg']
    if not os.path.exists(tar_dir):
            os.makedirs(tar_dir)
    for name in sample:
        shutil.copyfile(file_dir+"/"+name, f"{tar_dir}/{pre}{i}_{name}")
        i = i+step # 多文件错开


def multiple_dir(root_dir="img",outdir="", num=40,pre="",i=0,step =2):
    dir_list = list(
        filter(
            lambda x: not x.startswith(".")
                      and os.path.isdir(os.path.join(root_dir, x)),
            os.listdir(root_dir),
        )
    )
    for p in dir_list:
        path = os.path.join(root_dir, p)
        path_out = os.path.join(outdir, p)
        copy_file(path,path_out,num=num,pre=pre,i=i,step =step)


if __name__ == '__main__':
    file_dir = "/Users/liampro/Downloads/dataLake/images/图像分类/垃圾分类/DATASET_clean/TEST/O"
    tar_dir = "/Users/liampro/Downloads/dataLake/images/图像分类/垃圾分类/DATASET_clean/temp/O2"
    num = 10
    copy_file(file_dir=file_dir,tar_dir=tar_dir,num=num,step =1)
