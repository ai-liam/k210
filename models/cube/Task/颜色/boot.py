import sensor, image, lcd, time
import gc, sys

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

def main(sensor_window=(224, 224), lcd_rotation=0, sensor_hmirror=False, sensor_vflip=False):
    def draw_string(img, x, y, text, color, scale, bg=None ):
        if bg:
            img.draw_rectangle(x-2,y-2, len(text)*8*scale+4 , 16*scale, fill=True, color=bg)
        img = img.draw_string(x, y, text, color=color,scale=scale)
        return img

    sensor.reset()
    sensor.set_pixformat(sensor.RGB565)
    sensor.set_framesize(sensor.QVGA)
    sensor.skip_frames(time = 2000)
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
    print("Color start run")
    lcd.clear(lcd.WHITE)
    green_threshold   = (0,   80,  -70,   -10,   -0,   30)
    #red[0],green[1],blue[2]
    rgb_thresholds   =[(30, 100, 15, 127, 15, 127),(0, 80, -70, -10, -0, 30), (0, 30, 0, 64, -128, -20)]   #view in IDE
    ts_thresholds = [(40, 47, -128, 44, 16, 127),(79, 90, -128, 127, 5, 30)]
    try:
        while(True):
            img = sensor.snapshot()
            if board_cube:
               img = img.resize(img_size[0], img_size[1])
               img = img.rotation_corr(z_rotation=90)
               #img.pix_to_ai()
            # do work
            blobs = img.find_blobs(ts_thresholds)
            if blobs:
               for b in blobs:
                   tmp=img.draw_rectangle(b[0:4]) # rect
                   tmp=img.draw_cross(b[5], b[6]) # cx, cy
                   c=img.get_pixel(b[5], b[6])
                   print(b)

            # {"x":4, "y":27, "w":2, "h":6, "pixels":14, "cx":4, "cy":30, "rotation":1.328557, "code":1, "count":1}
            # draw
            img.draw_string(0, 200, "img color:", color=lcd.RED,scale=2)
            lcd.display(img)
            time.sleep_ms(100)

    except Exception as e:
        raise e
    finally:
        pass

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        sys.print_exception(e)
        lcd_show_except(e)
    finally:
        gc.collect()
