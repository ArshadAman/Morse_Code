MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
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
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'}

MORSE_INVERTED = {value: key for key, value in MORSE_CODE_DICT.items()}

def encrypt(text):
    morse_code = ""
    for letter in text:
        if letter != " ":
            morse_code = morse_code + MORSE_CODE_DICT[letter]+" "
        else:
            morse_code += " "

    return morse_code

def decrypt(morse_code):
    text = ""
    for morse in morse_code:
        if morse != " ":
            text += text + MORSE_INVERTED[morse]+ " "
        else:
            text += " "



def main():
    message = input("Enter your message: ").upper()
    e_or_d = input("Encryption(e) or decreption(d): ").lower()
    
    if e_or_d == "e":
        print(encrypt(message))
    elif e_or_d == "d":
        print(decrypt(message))
    else:
        print("Invalid Input")
        main()

if __name__ == "__main__":
    main()



    



