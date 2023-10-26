import board
import digitalio
import time
import adafruit_mpu6050                        #importing accelerometer libraries
import busio                                                
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio


displayio.release_displays()
sda_pin = board.GP14                                                #defines pin 14 and 15 as SDA and SCL pins
scl_pin = board.GP15                                                #needs to be pins 14 and 15 because they are in the sam I2C bus              
i2c = busio.I2C(scl_pin, sda_pin)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP0)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)                                              
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)                   #initializes the sensor
led = digitalio.DigitalInOut(board.GP1)                             #initializing led pins and outputs
led.direction = digitalio.Direction.OUTPUT   

splash = displayio.Group()
title = "ANGULAR VELOCITY"
text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
splash.append(text_area)
display.show(splash)

while True:
    
    print(f"x acceleration {mpu.acceleration[0]:.3f}")          #uses a f string to print the x,y, and z values
    print(f"y acceleration {mpu.acceleration[1]:.3f}")          #:.3f limits output to 3 decimals
    print(f"z acceleration {mpu.acceleration[2]:.3f}\n")        #\n is pythons version of println, adds a space inbetween each group of readings
    time.sleep(.01)    
    
    if mpu.acceleration[0] > .5:   #if the accelerometer is tilted more than 90 degrees turn on the light
        led.value = True
    else:
        led.value = False                                   #if not 90 degrees, keep the light off
    
   

    text_area.text = f"X={mpu.gyro[0]:.3f}\nY={mpu.gyro[1]:.3f}\nZ={mpu.gyro[2]:.3f}"

    time.sleep(.01)
    
