#!/bin/bash
shell_dir=$(dirname $0)
cd ${shell_dir}
ncc_dir="./"

echo "start run"

if [[ ! $1 ]]; then
    echo "path is null"; exit 1;
else
    echo "path：$1"
fi

if [[ ! $2 ]]; then
    echo "path is null"; exit 1;
    ncc_dir="./ncc-linux-x86_64/ncc"
else
    echo "path：$2"
    ncc_dir=$2
fi

${ncc_dir} -i tflite -o k210model --dataset ./$1/sample_images ./$1/m.tflite ./$1/result/m.kmodel

echo "start end"
# ./tokmodel.sh out/yolo_1