# object classifier boot.py

import sensor, image, lcd, time
import KPU as kpu
import gc, sys

from Maix import utils
import machine

board_cube = 1

def lcd_show_except(e):
    import uio
    err_str = uio.StringIO()
    sys.print_exception(e, err_str)
    err_str = err_str.getvalue()
    img = image.Image(size=(224,224))
    img.draw_string(0, 10, err_str, scale=1, color=(0xff,0x00,0x00))
    lcd.display(img)

def main(model_addr=0x300000, sensor_window=(224, 224), lcd_rotation=0, sensor_hmirror=False, sensor_vflip=False):
    labels = ["1","2","3","4","5","6","7"]
    def draw_string(img, x, y, text, color, scale, bg=None ):
        if bg:
            img.draw_rectangle(x-2,y-2, len(text)*8*scale+4 , 16*scale, fill=True, color=bg)
        img = img.draw_string(x, y, text, color=color,scale=scale)
        return img

    sensor.reset()
    sensor.set_pixformat(sensor.RGB565)
    sensor.set_framesize(sensor.QVGA)
    sensor.set_windowing(sensor_window)
    sensor.set_hmirror(sensor_hmirror)
    sensor.set_vflip(sensor_vflip)

    if board_cube == 1:
        sensor.set_vflip(True)
        sensor.set_hmirror(True)
        lcd.init(type=2)
        lcd.rotation(2)
    else:
        lcd.init()
        lcd.rotation(lcd_rotation)

    sensor.run(1)
    lcd.clear(lcd.WHITE)
    print("AA start 3")
    task = kpu.load(model_addr)
    a = kpu.set_outputs(task, 0, 5, 1, 1)
    print("start 5")
    try:
        while(True):
            print("start 66")
            img = sensor.snapshot()
            if board_cube:
               img = img.rotation_corr(z_rotation=90)
               img.pix_to_ai()

            #img2 = img.resize(64, 64)
            #a = img2.invert()
            #a = img2.strech_char(1)
            #a = img2.pix_to_ai()
            t = time.ticks_ms()
            fmap = kpu.forward(task, img)
            t = time.ticks_ms() - t
            plist=fmap[:]
            pmax=max(plist)
            print("plist:",plist)
            max_index=plist.index(pmax)
            print(max_index)
            #img.draw_string(0,0, "AP:%.2f C: %s" %(pmax, labels[max_index].strip()), scale=2)
            #img = draw_string(img, 2, 2, "NoC: %d P: %.2f" % (labels[max_index], pmax), color=lcd.WHITE,scale=2, bg=lcd.RED)
            img = draw_string(img, 2, 2, "NoC: %s P: %.2f" % (labels[max_index], pmax), color=lcd.WHITE,scale=2, bg=lcd.RED)

            #img.draw_string(0, 200, "t:%dms" %(t), scale=2)
            lcd.display(img)
            time.sleep_ms(100)

    except Exception as e:
        raise e
    finally:
        kpu.deinit(task)

def gc_resize():
    utils.gc_heap_size(256*1024)
    machine.reset()

if __name__ == "__main__":
    try:
        #gc_resize()
        main( model_addr=0x300000)
        #main( model_addr="/sd/models/garbage_210915.kmodel")
    except Exception as e:
        sys.print_exception(e)
        lcd_show_except(e)
    finally:
        gc.collect()
