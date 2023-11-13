import board
import digitalio
import time

led = digitalio.DigitalInOut(board.GP1)
led.direction = digitalio.Direction.OUTPUT

MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',            #collection of letters and their morse code equivalents 
    '(':'-.--.', ')':'-.--.-', ' ': '/'}                #added ' ':'/' to add a slash in -between words

modifier = 0.25
dot_time = 1*modifier
dash_time = 3*modifier
between_taps = 1*modifier
between_letters = 3*modifier
between_words = 7*modifier

while True:
    string = input("Enter message or -Q to quit: ")
    if string == '-Q':                                  #breaks while true if -Q is input
        break

    string = string.upper()
    temp = ""
    for x in range(len(string)):                        #for each letter, adds morse code equivalent to string
        temp += MORSE_CODE[string[x]] + " "
    print(f"{temp} ")                                   #f string allows to add space in between each letter

    for y in temp:
        if y == '.':
            led.value = True
            time.sleep(dot_time)
            led.value = False
        if y == '-':
            led.value = True
            time.sleep(dash_time)
            led.value = False
        if y == ' ':
            led.value = True
            time.sleep(between_letters)
            led.value = False
        if y == '/':
            led.value = True
            time.sleep(between_words)
        led.value = False    
        time.sleep(between_letters)