
import sensor,image,lcd,time
import KPU as kpu
import gc, sys

board_cube = 1

def main(model_addr=0x300000, lcd_rotation=0, sensor_hmirror=False, sensor_vflip=False):
    classes = ['aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car', 'cat', 'chair', 'cow', 'diningtable', 'dog', 'horse', 'motorbike', 'person', 'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor']
    try:
        sensor.reset(freq=24000000, set_regs=True, dual_buff=True)
        sensor.set_auto_gain(1)
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

    clock = time.clock()

    try:
        task = None
        task = kpu.load(model_addr)
        anchor = (1.889, 2.5245, 2.9465, 3.94056, 3.99987, 5.3658, 5.155437, 6.92275, 6.718375, 9.01025)
        #init yolo2 ,0.7（70%）
        a = kpu.init_yolo2(task, 0.7, 0.3, 5, anchor)
        lcd.clear(lcd.WHITE)

        while(True):
            clock.tick()
            img = sensor.snapshot()
            if board_cube:
                img = img.rotation_corr(z_rotation=90)
                img.pix_to_ai()

            code = kpu.run_yolo2(task, img)
            if code:
                for i in code:
                    a=img.draw_rectangle(i.rect())
                    img.draw_string(i.x(), i.y(), classes[i.classid()], color=(230,125,0), scale=2, mono_space=0)
                    #print(classes[i.classid()])
                    img.draw_string(i.x(), i.y()+12, '%f1.3'%i.value(), color=(230,150,0), scale=2, mono_space=0)
                    fps =clock.fps()
                    img.draw_string(50,10, ("c20 t: %2.1ffps" %(fps)), color=(0,128,0), scale=2)
                    img.draw_string(50,200, ("name: %s" %(classes[i.classid()])), color=(0,128,0), scale=3)
                    a = lcd.display(img)
            else:
                fps =clock.fps()
                img.draw_string(50,10, ("c20 nt: %2.1ffps" %(fps)), color=(0,128,0), scale=2)
                a = lcd.display(img)
            time.sleep_ms(30)

    except Exception as e:
        raise e
    finally:
        if not task is None:
            kpu.deinit(task)

def lcd_show_except(e):
    import uio
    err_str = uio.StringIO()
    sys.print_exception(e, err_str)
    err_str = err_str.getvalue()
    img = image.Image(size=(224,224))
    img.draw_string(0, 10, err_str, scale=1, color=(0xff,0x00,0x00))
    lcd.display(img)

def run():
    print("start class 20")
    try:
        #main( model_addr=0x300000 ,lcd_rotation=1, sensor_hmirror=False, sensor_vflip=False)
        main(model_addr="/sd/models/m3/class20_210915.kmodel",lcd_rotation=1, sensor_hmirror=False, sensor_vflip=False)
    except Exception as e:
        sys.print_exception(e)
        lcd_show_except(e)
    finally:
        gc.collect()

if __name__ == "__main__":
    print("start class 20")
    run()
