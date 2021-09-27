# 训练

    支持本地训练，百度AI平台，Google colab 平台训练。
    支持分类模型，目标检测模型的训练。
    详情看相关 notebook 脚本。

## 在线训练

- 百度AI平台
  
  [分类](https://aistudio.baidu.com/aistudio/projectdetail/2410414?channel=0&channelType=0&shared=1)

  [检测](https://aistudio.baidu.com/aistudio/projectdetail/2412779?channel=0&channelType=0&shared=1)

- Google colab
  
    在colab平台打开
    
    xl-classifier_colab_v1.ipynb ,
    
    xl-detector_colab_v1.ipynb
    
    就可以训练了。

## 本地训练环境搭建

建议安装 Anaconda管理python环境。

``` shell

conda create -n k210v37 python=3.7
conda activate k210v37

pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
or
pip3 install -r requirements.txt
```

启动 jupyterlab 打开 xl-classifier-local_v3.ipynb 就可以在本地跑模型了。

## 训练要注意点

[注意点](
https://wiki.sipeed.com/soft/maixpy/zh/course/image/basic/vary.html)

[MaixPy AI 硬件加速基本知识](
https://wiki.sipeed.com/soft/maixpy/zh/course/ai/basic/maixpy_hardware_ai_basic.html)

[K210 和 KPU](
https://github.com/kendryte/nncase/blob/master/docs/FAQ_ZH.md)

## 资源

[详情](
https://github.com/zhen8838/K210_Yolo_framework)
