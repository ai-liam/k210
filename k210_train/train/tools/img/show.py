import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

# 1层目录
def show_img(path="./img/a", num = 4 ,label =""):
    img_dir = os.listdir(path)
    i = 0

    plt.figure(figsize=(12, 6)) # 10 10
    for name in img_dir:
        ax = plt.subplot(2, 4, i + 1) # 3 3
        file_path = os.path.join(path,name) #path + img
        img = mpimg.imread(file_path)
        plt.imshow(img)
        plt.title(name)
        plt.title(label,y=1,loc='left')
        plt.axis("off")
        i= i+1
        if i >= num:
            break
# 2层目录
def show_multiple_dir(root_dir="img",num=4):
    dir_list = list(
        filter(
            lambda x: not x.startswith(".")
                      and os.path.isdir(os.path.join(root_dir, x)),
            os.listdir(root_dir),
        )
    )
    for p in dir_list:
        path = os.path.join(root_dir, p)
        #print("p:",p)
        show_img(path=path, num = num ,label =p)

