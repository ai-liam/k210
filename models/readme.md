# k210的cube可以运行的模型

把 cube/main复制到 sd 卡，SD 目录为
(base) liam18@liam main % tree
.
├── boot.py
├── cube_boot.py
└── models
    ├── 9ge.jpg
    ├── m1
    │   └── boot.py
    ├── m2
    │   ├── boot.py
    │   └── facedetect_210915.kmodel
    ├── m3
    │   ├── boot.py
    │   └── class20_210915.kmodel
    ├── m4
    │   └── boot.py
    ├── m5
    │   └── boot.py
    ├── m6
    │   └── boot.py
    ├── m7
    │   └── boot.py
    ├── m8
    │   └── boot.py
    ├── m9
    │   └── boot.py
    └── readme.txt

## 脸部检测

./cube/人脸检测/v1-0x00300000 : ok
（来源官方）

    任务：只是识别人脸

## 垃圾分类

./cube/垃圾分类/v0: 不成功
https://baike.baidu.com/item/%E5%9E%83%E5%9C%BE%E5%88%86%E7%B1%BB/2904193
https://aistudio.baidu.com/aistudio/datasetdetail/77996
    热门的主题；分5类：塑料制品｜塑料瓶｜纸杯和纸质容器｜残余饮料｜食物残渣、纸巾和筷子

## 交通标识

./cube/交通标识

    可以用做智慧交通

## 生活物品分类

./cube/生活物品分类

    比如椅子、桌子、书本笔等等。

## 数字识别

./cube/数字识别

    主要是识别数字，应用场景：如电表检测

## 通用多分类

./cube/通用多分类/v1: ok

    ['飞机'，'自行车'，'鸟'，'船'，'瓶子'，'公共汽车'，'汽车'，'猫'，'椅子'，'牛'，'餐桌'，'狗'， “马”、“摩托车”、“人”、“盆栽”、“羊”、“沙发”、“火车”、“电视监视器”]

## 二维码识别

models/cube/Task/二维码: ok

## 颜色识别

https://blog.csdn.net/weixin_45020839/article/details/118025480
在Maixpy IDE 选择【工具】——【机器视觉】——【阈值编辑器】


## config

https://github.com/sipeed/MaixPy_scripts/blob/master/board/config_maix_cube.py
