import board
import digitalio
import time
import adafruit_mpu6050                        #importing accelerometer libraries
import busio                                                

sda_pin = board.GP14                           #defines pin 14 and 15 as SDA and SCL pins
scl_pin = board.GP15                           #needs to be pins 14 and 15 because they are in the sam I2C bus
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)            #initializes the sensor
led = digitalio.DigitalInOut(board.GP1)        #initializing led pins and outputs
led.direction = digitalio.Direction.OUTPUT   


while True:
    print(f"x acceleration {mpu.acceleration[0]}")          #uses a f string to print the x,y, and z values
    print(f"y acceleration {mpu.acceleration[1]}")
    print(f"z acceleration {mpu.acceleration[2]}\n")        #\n is pythons version of println, adds a space inbetween each group of readings
    time.sleep(.1)    
    if mpu.acceleration[0] > .5:   #if the accelerometer is tilted more than 90 degrees turn on the light
        led.value = True
    else:
        led.value = False                                   #if not 90 degrees, keep the light off