# 处理tflive转kmodel

## 下载 ncc

    win,linux可以直接跑官方命令；
    tool:https://github.com/kendryte/nncase/releases/tag/v0.1.0-rc5

    Mac 要docker跑ubuntu环境，解压 ncc-linux-x86_64 到这里。

## mac例子

docker run -it -v /Users/liampro/Downloads/pro/git/ai-test/k210/ubuntu:/train ubuntu /train/tokmodel.sh out/imgn_2021-09-16_15_58

## linux例子

./ncc-linux-x86_64/ncc -i tflite -o k210model --dataset ./out_imgn/sample_images ./out_imgn/m.tflite ./out_imgn/v3_c2_210915.kmodel

## win例子

./ncc.exe -i tflite -o k210model --dataset ./out_imgn/sample_images ./out_imgn/m.tflite ./out_imgn/v3_c2_210915.kmodel

## 问题

ubuntu环境无法跑？
解决：用 bug/ncc.runtimeconfig.json 取代 ncc-linux-x86_64/ncc.runtimeconfig.json

权限问题？(可读可写可执行)
chmod 777 ./
