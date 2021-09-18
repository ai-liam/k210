# kmodel

转换工具：https://github.com/kendryte/nncase/releases/tag/v0.1.0-rc5

## 如何编译kmodel V4

V4模型大于1.5M 无法跑（用 k210-NNCasev0.2.0Beta2 编译）
./ncc compile ./out/c2.tflite ./out/c2a.kmodel -i tflite -o kmodel --dataset ./out/sample_images

## 如何编译kmodel V3

### 用 nnc v0.1.0-rc5 版本 制作v3 版本的kmodel

### 用ubuntu环境编译

生成容器运行：
docker run -it -v /Users/liampro/Downloads/pro/git/ai-test/k210/ubuntu:/train ubuntu /bin/bash

直接生成kmodel:
docker run -it -v /Users/liampro/Downloads/pro/git/ai-test/k210/ubuntu:/train ubuntu /train/tokmodel.sh out/yolo_1

./ncc-linux-x86_64/ncc -help

出现问题，修改：ncc.runtimeconfig.json 如下
    {
        "runtimeOptions": {
            "configProperties": {
                "System.Globalization.Invariant": true
            }
        }
    }

cd train

imagesnet:
./ncc-linux-x86_64/ncc -i tflite -o k210model --dataset ./out_imgn/sample_images ./out_imgn/m.tflite ./out_imgn/v3_c2_210915.kmodel

yolo:
./ncc-linux-x86_64/ncc -i tflite -o k210model --dataset ./out_yo/sample_images ./out_yo/m.tflite ./out_yo/v3_y2a.kmodel

## 问题

1. ubuntu中ncc无法运行
http://www.uims.top/docs/dotnet.cn/core/run-time-config/globalization.html

2. V3kmodel无法运行
可跑官网生成kmodel固件：
maixpy_v0.6.2_67_g42d3cf611_minimum_with_ide_support.bin
建议用下面的
maixpy_v0.6.2_67_g42d3cf611_openmv_kmodel_v4_with_ide_support.bin

大于1.5M固件无法跑

## 小结

模型可以正常运行，训练了。准确率要提高。
