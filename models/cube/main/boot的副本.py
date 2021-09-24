import sensor, image, lcd, time
import gc, sys
import models.m1.boot as m1
import models.m2.boot as m2
import models.m3.boot as m3

# config change for youself
img_size = [224,224]
#labels = ['0', '1', '2']
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
    print("Test start run")
    lcd.clear(lcd.WHITE)
    ts = m1.test("hi")
    print(ts)
    m3.run()
    #while(True):
        #loop()

def loop():
    try:
        img = sensor.snapshot()
        if board_cube:
            img = img.resize(img_size[0], img_size[1])
            img = img.rotation_corr(z_rotation=90)
            img.pix_to_ai()
        img.draw_string(0, 200, "imgTest main", color=lcd.RED,scale=2)
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
