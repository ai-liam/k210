import sensor, image, lcd, time
import gc, sys

from Maix import GPIO
from fpioa_manager import fm

img_size = [224,224]
board_cube = 1
model_index = 1 # 1-9
run_state = 0 # 0 ,1 run model
model_num = 9 #1-9

# reg
fm.register(16, fm.fpioa.GPIOHS0) # 16 NEXT
fm.register(11, fm.fpioa.GPIOHS1) #11 BACK
fm.register(10, fm.fpioa.GPIOHS2) #10 ENTER
key_next = GPIO(GPIO.GPIOHS0, GPIO.PULL_UP) # 0
key_back = GPIO(GPIO.GPIOHS1, GPIO.PULL_UP) # 0
key_enter = GPIO(GPIO.GPIOHS2, GPIO.PULL_UP) # 0
img9 = image.Image("/sd/models/9ge.jpg")

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


def client_next():
    global model_index
    if run_state == 0 and key_next.value() == 0 and model_index < 9:
        model_index = model_index +1
        time.sleep_ms(100)
        print("client_next:",model_index)


def client_back():
    global model_index
    if run_state == 0 and key_back.value() == 0 and model_index >1 :
        model_index = model_index - 1
        time.sleep_ms(100)
        print("client_back:",model_index)

def client_enter():
    if run_state == 0 and key_enter.value() == 0 :
        return True
        #enter_model(model_index)
    return False

def next_model(img,_index):
    if _index < 0 or _index > 9:
        _index = 1
    i = _index -1
    _w = int(img_size[0] / 3)
    x = int(i % 3) * _w
    y = int(i / 3) * _w
    img.draw_rectangle((x, y, _w, _w), color=lcd.RED)

def enter_model(_index):
    global run_state
    run_state = 1
    if _index == 1:
        import models.m1.boot as m1
        m1.run()
    elif _index == 2:
        import models.m2.boot as m2
        m2.run()
    elif _index == 3:
        import models.m3.boot as m3
        m3.run()
    elif _index == 4:
        import models.m4.boot as m4
        m4.run()
    elif _index == 5:
        import models.m5.boot as m5
        m5.run()
    elif _index == 6:
        import models.m6.boot as m6
        m6.run()
    elif _index == 7:
        import models.m7.boot as m7
        m7.run()
    elif _index == 8:
        import models.m8.boot as m8
        m8.run()
    elif _index == 9:
        import models.m9.boot as m9
        m9.run()


def loop():
    try:
        #print("key next:",str(key_next.value()))
        #print("key back:",str(key_back.value()))
        #print("key enter:",str(key_enter.value()))
        #img = image.Image("/sd/models/9ge.jpg")
        #img = sensor.snapshot()
        img = img9.copy()
        img.draw_string(0, 200, "imgTest main", color=lcd.RED,scale=2)
        client_next()
        client_back()
        if client_enter() and model_index <= model_num:
            del img
            enter_model(model_index)
            time.sleep_ms(100)
        next_model(img,model_index)
        lcd.display(img)
        time.sleep_ms(100)
    except Exception as e:
        raise e
    finally:
        pass

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
    #ts = m1.test("hi")
    #print(ts)
    #m3.run()

    #_thread.start_new_thread(thread_listem1,(0,))
    while(True):
        loop()

def clean():
    fm.unregister(16)
    fm.unregister(11)
    fm.unregister(10)

def run():
    try:
        main()
    except Exception as e:
        sys.print_exception(e)
        lcd_show_except(e)
    finally:
        clean()
        gc.collect()



if __name__ == "__main__":
    run()
