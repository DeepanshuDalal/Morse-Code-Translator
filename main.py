# MORSE CODE DECODER

morse_code = {
    "a":".-",
    "b":"-...",
    "c":"-.-.",
    "d":"-..",
    "e":".",
    "f":"..-.",
    "g":"--.",
    "h":"....",
    "i":"..",
    "j":".---",
    "k":"-.-",
    "l":".-..",
    "m":"--",
    "n":"-.",
    "o":"---",
    "p":".--.",
    "q":"--.-",
    "r":".-.",
    "s":"...",
    "t":"-",
    "u":"..-",
    "v":"...-",
    "w":".--",
    "x":"-..-",
    "y":"-.--",
    "z":"--..",
    "0":"-----",
    "1":".----",
    "2":"..---",
    "3":"...--",
    "4":"....-",
    "5":".....",
    "6":"-....",
    "7":"--...",
    "8":"---..",
    "9":"----."
}

def encode(message):
    message = message

    code_list = []
    
    for word in message:
        for letter in word:

            if letter == "/":
                code_list.append("/")
            else:
                alpha = morse_code[letter]
                code_list.append(alpha)
    code = " ".join(code_list)
    print(code)

def decode(code_string):
    code_string = code_string
    
    # interchanging morse_code dict index and value to decode morse code
    rev_morse_code = dict((v,k) for k,v in morse_code.items())

    decode_list = []

    for code in code_string:

        if code == "/":
            decode_list.append(" ")
        else:
            text = rev_morse_code[code]
            decode_list.append(text)

    # converting list into string
    decoded_message = ""
    for code in decode_list:
        letter = str(code)
        if letter == " ":
            decoded_message += " "
        else:
            decoded_message += letter

    print(decoded_message)


choice = input("Enter 'E' for encoding and 'D' for decoding: ").lower()
if choice == "e":
    message = input("Enter your message to encode: ").lower().split(" ")

    # inserting "/" in every other position in the list to use it as a space.
    for blanks in range(0,len(message)):
        message.insert(blanks*2,"/")
    
    # removing the first "/" because its not needed, as no sentence start with the space.
    message.pop(0)
    encode(message)
elif choice == "d":
    code = input("Enter your code to decode (input / instead of space between words): ").lower().split(" ")
    decode(code)
else:
    print("Invalid Input!!!")


