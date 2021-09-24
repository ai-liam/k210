# object detector boot.py

import sensor, image, lcd, time
import KPU as kpu
import gc, sys

# config change for youself
labels = ["0", "1"] # labels
anchors = [3.28125, 3.28125] # anchors
img_size = [224,224] # img_size
#labels = ['0', '1', '2']
#anchors =[3.28125, 3.28125, 1.6875, 1.78125, 4.25, 4.09375, 5.15625, 5.15625, 2.4375, 2.40625]
#img_size = [224,224]
board_cube = 1

def lcd_show_except(e):
    import uio
    err_str = uio.StringIO()
    sys.print_exception(e, err_str)
    err_str = err_str.getvalue()
    img = image.Image(size=(img_size[0],img_size[1]))
    img.draw_string(0, 10, err_str, scale=1, color=(0xff,0x00,0x00))
    lcd.display(img)

def main( model_addr="/sd/m.kmodel", lcd_rotation=0, sensor_hmirror=False, sensor_vflip=False):
    try:
        sensor.reset()
    except Exception as e:
        raise Exception("sensor reset fail, please check hardware connection, or hardware damaged! err: {}".format(e))

    sensor.set_pixformat(sensor.RGB565)
    sensor.set_framesize(sensor.QVGA)
    #sensor.set_windowing((img_size[0], img_size[1]))
    if board_cube == 1:
        sensor.set_vflip(True)
        sensor.set_hmirror(True)
        lcd.init(type=2)
        lcd.rotation(2)
    else:
        lcd.init(type=1)
        lcd.rotation(lcd_rotation)
        sensor.set_hmirror(sensor_hmirror)
        sensor.set_vflip(sensor_vflip)
        lcd.rotation(lcd_rotation)
    sensor.run(1)
    lcd.clear(lcd.WHITE)
    try:
        task = None
        task = kpu.load(model_addr)# stop in here!
        # 50%
        kpu.init_yolo2(task, 0.5, 0.3, 5, anchors) # threshold:[0,1], nms_value: [0, 1]
        while(True):
            img = sensor.snapshot()
            if board_cube:
                img = img.resize(img_size[0], img_size[1])
                img = img.rotation_corr(z_rotation=90)
                img.pix_to_ai()
            t = time.ticks_ms()
            objects = kpu.run_yolo2(task, img)
            t = time.ticks_ms() - t
            if objects:
                for obj in objects:
                    pos = obj.rect()
                    img.draw_rectangle(pos)
                    img.draw_string(pos[0], pos[1], "C: %s P: %.2f" %(labels[obj.classid()], obj.value()), scale=2, color=(255, 0, 0))
                    print(labels[obj.classid()])
            img.draw_string(0, 200, "yolov2 t:%dms" %(t), scale=2, color=(255, 0, 0))
            lcd.display(img)
            time.sleep_ms(100)
    except Exception as e:
        raise e
    finally:
        if not task is None:
           kpu.deinit(task)

def run():
    try:
        print("start: yolo")
        #main( model_addr=0x300000)
        main(model_addr="/sd/m.kmodel")
    except Exception as e:
        sys.print_exception(e)
        lcd_show_except(e)
    finally:
        gc.collect()    

if __name__ == "__main__":
    run()
