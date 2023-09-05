# type: ignore
import board
import digitalio
import.time

led = digitalio.DigitalInOut(board.GP2)
led.direction = digitalio.Direction.OUTPUT