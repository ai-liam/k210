#!/bin/bash
shell_dir=$(dirname $0)
cd ${shell_dir}

if [[ ! $1 ]]; then
    echo "path is null"; exit 1;
else
    echo "path：$1"
fi

if [[ ! $2 ]]; then
    echo "tflive is null"; exit 1;
else
    echo "tflive path：$2"
fi

echo "start docker"

#docker run -it -v /Users/liampro/Downloads/pro/git/ai-test/k210/ubuntu:/train ubuntu /train/tokmodel.sh out/yolo_2021-09-16_11_30
#/Applications/Docker.app/Contents/Resources/bin/docker run -it -v $1:/train ubuntu /train/tokmodel.sh $2

docker run -it -v $1:/train ubuntu /train/tokmodel.sh $2

# ./ncc-mac.sh /Users/liampro/Downloads/pro/git/ai-test/k210/ubuntu out/yolo_2021-09-16_11_30

# chmod -R 777 ./
