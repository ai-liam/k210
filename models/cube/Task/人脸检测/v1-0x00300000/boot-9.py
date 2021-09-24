import sensor, image, lcd, time
import KPU as kpu
import gc, sys

board_cube = 1

# is ok to run!

def lcd_show_except(e):
    import uio
    err_str = uio.StringIO()
    sys.print_exception(e, err_str)
    err_str = err_str.getvalue()
    img = image.Image(size=(224,224))
    img.draw_string(0, 10, err_str, scale=1, color=(0xff,0x00,0x00))
    lcd.display(img)

def main(model_addr=0x300000, lcd_rotation=0, sensor_hmirror=False, sensor_vflip=False):
    try:
        sensor.reset()
    except Exception as e:
        raise Exception("sensor reset fail, please check hardware connection, or hardware damaged! err: {}".format(e))

    sensor.set_pixformat(sensor.RGB565)
    sensor.set_framesize(sensor.QVGA)
    #sensor.skip_frames()
    #sensor.set_windowing((224, 224))
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

    anchors = (1.889, 2.5245, 2.9465, 3.94056, 3.99987, 5.3658, 5.155437, 6.92275, 6.718375, 9.01025)
    try:
        task = None
        task = kpu.load(model_addr)
        #init yolo2 ,0.5（50%）
        kpu.init_yolo2(task, 0.5, 0.3, 5, anchors) # threshold:[0,1], nms_value: [0, 1]
        while(True):
            img = sensor.snapshot()
            if board_cube:
                img = img.rotation_corr(z_rotation=90)
                img.pix_to_ai()
            t = time.ticks_ms()
            objects = kpu.run_yolo2(task, img)
            t = time.ticks_ms() - t
            if objects:
                #print("had face ")
                for obj in objects:
                    img.draw_rectangle(obj.rect())

            img.draw_string(48, 10, "FaceDetection t:%dms" %(t), scale=2)
            lcd.display(img)
            time.sleep_ms(100)

    except Exception as e:
        raise e
    finally:
        if not task is None:
            kpu.deinit(task)


if __name__ == "__main__":
    print("start face detection")
    try:
        main( model_addr=0x300000 ,lcd_rotation=1, sensor_hmirror=False, sensor_vflip=False)
        #main(model_addr="/sd/models/facedetect_210915.kmodel",lcd_rotation=1, sensor_hmirror=False, sensor_vflip=False)
    except Exception as e:
        sys.print_exception(e)
        lcd_show_except(e)
    finally:
        gc.collect()
