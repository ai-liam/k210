'''
    train detector

    @author neucrack@sipeed
    @license Apache 2.0 © 2020 Sipeed Ltd
'''



import sys, os
curr_file_dir = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(curr_file_dir)

#     import os, sys
# root_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
# sys.path.append(root_path)

from png2jpg import convert_dir,convert_multiple_dir
from clean import clean_dir ,clean_multiple_dir
from resize import resize_dir ,resize_multiple_dir
from generator import generator_dir ,generator_multiple_dir
from rename import rename_dir ,rename_multiple_dir

class Img():
    def __init__(self,clean=True,convert=True,resize=True,generator=False,rename=False,generator_num=2):
        self.clean = clean
        self.convert= convert
        self.resize = resize
        self.generator = generator
        self.rename = rename
        self.generator_num = generator_num

    def test(self,st=""):
        print("test:",st)

    def clean_dir_img(self,path="./img/a",outdir="",size=[224,224]):
        if self.clean:
            clean_dir(path=path, remove_error_img= True,min_size=[10,10])
        if self.convert:
            convert_dir(path)
        if self.resize:
            resize_dir(path=path,outdir=outdir, size=size,is_crop= True)
        if self.generator:
            generator_dir(path=path,num=self.generator_num)
        if self.rename:
            rename_dir(path=path,pre='')

    def clean_multiple_dir_img(self,root_dir="./img",outdir="", size=[224,224]):  
        if self.clean:
            clean_multiple_dir(root_dir=root_dir, remove_error_img= True,min_size=[10,10])
        if self.convert:
            convert_multiple_dir(root_dir=root_dir)
        if self.resize:
            resize_multiple_dir(root_dir=root_dir,outdir=outdir, size=size,is_crop= True)
        if self.generator:
            generator_multiple_dir(root_dir=root_dir,num=self.generator_num)
        if self.rename:
            rename_multiple_dir(root_dir=root_dir,pre='')


if __name__ == "__main__":
#    i = Img()
#    i.test("./img/a")
    path ="/Users/liampro/Downloads/dataLake/images/图像分类/垃圾分类/DATASET_clean/temp"
    img = Img(clean=True,convert=False,resize=False,generator=False)
    path1 =path+"/O"
    img.clean_dir_img(path= path1,size = [224,224])
   

