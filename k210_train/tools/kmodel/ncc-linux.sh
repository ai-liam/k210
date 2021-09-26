#!/bin/bash
shell_dir=$(dirname $0)
cd ${shell_dir}

if [[ ! $1 ]]; then
    echo "exe path is null"; exit 1;
else
    echo "exe path：$1"
fi

if [[ ! $2 ]]; then
    echo "tflive is null"; exit 1;
else
    echo "tflive path：$2"
fi

echo "start 1"

../../ubuntu/tokmodelv2.sh $1 $2
