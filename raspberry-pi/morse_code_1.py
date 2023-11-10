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


while True:
    string = input("Enter message or -Q to quit: ")
    if string == '-Q':                                  #breaks while true if -Q is input
        break

    string = string.upper()
    temp = ""
    for x in range(len(string)):                        #for each letter, adds morse code equivalent to string
        temp += MORSE_CODE[string[x]] + " "
    print(f"{temp} ")                                   #f string allows to add space in between each letter