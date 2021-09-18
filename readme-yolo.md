# YOLO

标注工具：https://github.com/tzutalin/labelImg

## yolov2 k210现在只支持v2

https://github.com/longcw/yolo2-pytorch

### 环境V2

source ~/.bash_profile
conda info -e
conda create -n yolov2 python=3.6
conda activate yolov2

conda activate yolov2 --default
conda remove -n yolov2 --all

### 安装依赖V2

cd temp/yolo2-pytorch
pip install -r requirements.txt

### 小结V2

本地跑不起来，太老了。

## yolov5

https://github.com/ultralytics/yolov5

### python环境V5

source ~/.bash_profile
conda info -e
conda create -n yolov5 python=3.8
conda activate yolov5

conda activate yolov5 --default
conda remove -n yolov5 --all

### 安装依赖V5

cd temp/object-detection/yolov5
pip install -r requirements.txt

### 测试V5

```shell
$ python detect.py --source 0  # webcam
                            file.jpg  # image 
                            file.mp4  # video
                            path/  # directory
                            path/*.jpg  # glob
                            'https://youtu.be/NUsoVlDFqZg'  # YouTube video
                            'rtsp://example.com/media.mp4'  # RTSP, RTMP, HTTP stream

```

python detect.py --source data/images/zidane.jpeg --weights yolov5s.pt --conf 0.25
测试成功。
