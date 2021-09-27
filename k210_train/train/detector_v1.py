import os, sys
import shutil
import time
import traceback

curr_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(curr_dir)

from detector import Detector
from utils.logger import Logger, Fake_Logger
from utils import gpu_utils, isascii
from detector.instance import config

def clear_save_path(temp_datasets_dir=""):
    if temp_datasets_dir =="":
        return False
    #clear
    if os.path.exists(temp_datasets_dir):
        shutil.rmtree(temp_datasets_dir)
    os.makedirs(temp_datasets_dir)
    return True

def creat_sample_images(detector,temp_datasets_dir="",sample_image_num = 20):
    dataset_sample_images_path = os.path.join(temp_datasets_dir, "sample_images")
    os.makedirs(dataset_sample_images_path)
    detector.get_sample_images(sample_image_num, dataset_sample_images_path)
    return True

def detector_train(datasets_zip_path="",datasets_dir="",temp_datasets_dir="",config= config):
    #clear and creat
    clear_save_path(temp_datasets_dir)
    log = Logger(file_path=f"{temp_datasets_dir}train_log.log")
    
    def __on_train_progress(percent, msg):  # flag: progress
        percent = percent*0.97 + 1
        log.i(f"progress: {percent}%, {msg}")
    
    # 检测 GPU 可用,选择一个可用的 GPU 使用
    try:
        gpu = gpu_utils.select_gpu(memory_require = config.detector_train_gpu_mem_require, tf_gpu_mem_growth=False)
    except Exception:
        gpu = None
    if gpu is None:
        if not config.allow_cpu:
            log.e("no free GPU")
            raise Exception(("TrainFailReason.ERROR_NODE_BUSY", "node no enough GPU or GPU memory and not support CPU train"))
        log.i("no GPU, will use [CPU]")
    else:
        log.i("select", gpu)

    # set value
    best_h5_model_path  = os.path.join(temp_datasets_dir, "m_best.h5")
    final_h5_model_path = os.path.join(temp_datasets_dir, "m.h5")
    result_dir = os.path.join(temp_datasets_dir, "result")
    os.makedirs(result_dir)
    result_report_img_path = os.path.join(result_dir, "report.jpg")
    tflite_path = os.path.join(temp_datasets_dir, "m.tflite")
    
    # 启动训练
    try:
        detector = Detector(input_shape=(224, 224, 3),
                            datasets_zip=datasets_zip_path,
                            datasets_dir=datasets_dir,
                            unpack_dir = temp_datasets_dir,
                            logger=log,
                            max_classes_limit = config.detector_train_max_classes_num,
                            one_class_min_images_num=config.detector_train_one_class_min_img_num,
                            one_class_max_images_num=config.detector_train_one_class_max_img_num,
                            allow_reshape = False)
    except Exception as e:
        log.e("train datasets not valid: {}".format(e))
        raise Exception(("TrainFailReason.ERROR_PARAM", "datasets not valid: {}".format(str(e))))
    try:

        f,anchors = detector.train(epochs=config.detector_train_epochs,
                progress_cb= __on_train_progress,
                save_best_weights_path = best_h5_model_path,
                save_final_weights_path = final_h5_model_path,
                jitter=False,
                is_only_detect = False,
                batch_size = config.detector_train_batch_size,
                train_times = 5,
                valid_times = 2,
                learning_rate=config.detector_train_learn_rate,
            )
        print("anchors 2:",anchors)
    except Exception as e:
        log.e("train error: {}".format(e))
        traceback.print_exc()
        raise Exception(("TrainFailReason.ERROR_INTERNAL", "error occurred when train, error: {}".format(str(e)) ))

    ## sample_image
    creat_sample_images(detector,temp_datasets_dir,config.sample_image_num)
    
    ## creat tflite
    detector.save(h5_path=final_h5_model_path)
    detector.save(tflite_path=tflite_path)
    
    # 训练结束, 生成报告
    log.i("train ok, now generate report")
    detector.report(result_report_img_path)
    
    return True , detector,final_h5_model_path,anchors , detector.get_labels()

def main(datasets_dir= ""):
    cur_time = time.strftime("%Y-%m-%d_%H_%M", time.localtime())
    ubuntu_path = f"out/yolo_{cur_time}" #用来mac中生成kmodel
    #os.path.join(curr_dir, "out")
    temp_saves_dir = os.path.join(curr_dir, "../../ubuntu",ubuntu_path)#f"../ubuntu/{ubuntu_path}/" #保存文件目录
    print("temp_saves_dir:",temp_saves_dir)
    if datasets_dir =="":
        datasets_dir =  os.path.join(curr_dir,"../../datasets/ts_xml_format")#数据源
    print("datasets_dir:",datasets_dir)
    config.detector_train_epochs = 1 # 修改训练轮数 40
    result,obj,model_path ,anchors,labels = detector_train(datasets_dir=datasets_dir,temp_datasets_dir=temp_saves_dir,config=config)
    print("model_path:",model_path)
    print("anchors:",anchors)
    print("labels:",labels)
    return result,obj,model_path ,anchors,labels

if __name__ == "__main__":
    sys.exit(main())