import board
import digitalio
import time

led = digitalio.DigitalInOut(board.GP1)         #Initializing led pins and outputs
led.direction = digitalio.Direction.OUTPUT      
led2= digitalio.DigitalInOut(board.GP2)
led2.direction = digitalio.Direction.OUTPUT


for x in range (10):                            #prints numbers 1-10 in ascending order
    print(10-x)                                 #changes to print numbers 1-10 in descending order
    led.value = True                            #blinks on and off every second
    time.sleep(.5)
    led.value = False
    time.sleep(.5)

print ("liftoff")
while True:                                     #Need a loop to continue running code after for loop
    led2.value = True                           #Turns on green led after countdown