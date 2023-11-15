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
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
t = 0
X = 0
Y = 0
X = 0
tilt = False

with open("/data.csv", "a") as datalog:

    while True:
        X = mpu.acceleration[0]      
        Y = mpu.acceleration[1]
        Z = mpu.acceleration[2]    
        t = time.monotonic()
           
        if mpu.acceleration[0] > .5:   #if the accelerometer is tilted more than 90 degrees turn on the light
            led.value = True
            tilt = True
        else:
            led.value = False
            tilt = False                              
        
        datalog.write(f"{t},{X},{Y},{Z},{tilt}\n")
        
        led.value = True
        time.sleep(.15)
        led.value = False
        
        datalog.flush()
        time.sleep(0.25)
