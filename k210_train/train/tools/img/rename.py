
import os

#https://blog.csdn.net/wearge/article/details/77374150
#

def rename_dir(path="./img/a",pre=''):
    #path='/home/huiyu/PycharmProjects/faceCodeByMe/testdata'
    #path :表示你需要批量改的文件夹
    i=0
    for item in os.listdir(path):#进入到文件夹内，对每个文件进行循环遍历
        if (item.endswith('.jpg') or item.endswith('.jpeg') or item.endswith('.JPG') or item.endswith('.png') or item.endswith('.PNG') ):
            ex = os.path.splitext(item)[1]
            #name = (pre+str(i)+ ex) # 123.jpg
            name = (str(i) + ex)
            #print('[name]:',name)
            try:
                os.rename(os.path.join(path,item),os.path.join(path,name))
                i+=1
            except Exception as e:
                print('[RENAME ERROR]:', os.path.join(path,item))
                print(e)
    print(f"[rename_dir {path} end]")

def rename_multiple_dir(root_dir,pre=''):
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
        rename_dir(path,p+pre)
    print('[rename_multiple_dir end]')

if __name__ == "__main__":
    path ="/Users/liampro/Downloads/dataLake/images/图像分类/垃圾分类/DATASET_clean/temp"
    path1 =path+"/O"
    rename_dir(path= path1 , pre='a_')
