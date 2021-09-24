# import os
# from PIL import Image

'''
from PIL import features
print (features.check_module('webp'))

is :False

conda install -c conda-forge libwebp
conda install -c conda-forge/label/gcc7 libwebp

conda install -c conda-forge/label/broken libwebp

conda install -c conda-forge/label/cf201901 libwebp

conda install -c conda-forge/label/cf202003 libwebp
'''

from PIL import Image
import PIL
import os
import glob

def webp2jpg(url="./img/a/1.webp"):
    try:
        out_file = os.path.splitext(url)[0] + "_webp.jpg"
        im = Image.open(url)
        im.convert("RGB")
        print("[save]:",out_file)
        im.save(out_file,  "jpeg")
    except Exception as e:
        print("[WebP转换JPG 错误file]:", url)
        print("[转换JPG 错误]:", e)



if __name__ == "__main__":
    path ="/Users/liampro/Downloads/temp/img/temp/1.webp"
    webp2jpg(url= path )
    from PIL import features
    print (features.check_module('webp'))
