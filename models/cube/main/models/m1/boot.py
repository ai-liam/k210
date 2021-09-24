# img code
import sensor, image, lcd, time
import gc, sys
from Maix import utils
import machine


img_size = [224,224]
board_cube = 1

def lcd_show_except(e):
    import uio
    err_str = uio.StringIO()
    sys.print_exception(e, err_str)
    err_str = err_str.getvalue()
    img = image.Image(size=(img_size[0],img_size[1]))
    img.draw_string(0, 10, err_str, scale=1, color=(0xff,0x00,0x00))
    lcd.display(img)

def draw_string(img, x, y, text, color, scale, bg=None ):
    if bg:
        img.draw_rectangle(x-2,y-2, len(text)*8*scale+4 , 16*scale, fill=True, color=bg)
    img = img.draw_string(x, y, text, color=color,scale=scale)
    return img

def main(sensor_window=(224, 224), lcd_rotation=0, sensor_hmirror=False, sensor_vflip=False):
    sensor.reset()
    sensor.set_pixformat(sensor.RGB565)
    sensor.set_framesize(sensor.QVGA)
    sensor.set_windowing((img_size[0], img_size[1]))
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
    print("AA start run")
    lcd.clear(lcd.WHITE)

    try:
        while(True):
            img = sensor.snapshot()
            if board_cube:
               img = img.resize(img_size[0], img_size[1])
               img = img.rotation_corr(z_rotation=90)
               img.pix_to_ai()

            res = img.find_qrcodes()
            if len(res) > 0:
                    img.draw_string(2,2, "is: %s" %res[0].payload(), color=(0,128,0), scale=3)
                    print(res[0].payload())
            img.draw_string(0, 200, "imgCode", color=lcd.RED,scale=2)
            #{"x":37, "y":32, "w":153, "h":154, "payload":"stop", "version":1, "ecc_level":2, "mask":0, "data_type":4, "eci":0}
            lcd.display(img)
            time.sleep_ms(100)

    except Exception as e:
        raise e
    finally:
        pass

def run():
    try:
        main()
    except Exception as e:
        sys.print_exception(e)
        lcd_show_except(e)
    finally:
        gc.collect()

if __name__ == "__main__":
    run()
