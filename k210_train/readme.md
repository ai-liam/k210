# 训练

## 环境

```
pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
or
pip3 install -r requirements.txt
```

## 转kmodel

'''shell
./tools/ncc compile ./out/m.tflite ./out/m1.kmodel -i tflite -o kmodel --dataset ./out/sample_images
'''

## 训练要注意点

https://wiki.sipeed.com/soft/maixpy/zh/course/image/basic/vary.html

MaixPy AI 硬件加速基本知识:
https://wiki.sipeed.com/soft/maixpy/zh/course/ai/basic/maixpy_hardware_ai_basic.html

K210 和 KPU:
https://github.com/kendryte/nncase/blob/master/docs/FAQ_ZH.md

## 资源：
https://github.com/zhen8838/K210_Yolo_framework

