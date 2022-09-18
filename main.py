Morse_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def encrypt(message):
    Morse = ''
    for letter in message:
        if letter != ' ':
            Morse += Morse_CODE_DICT[letter.upper()] + ' '
        else:
            Morse += '-....- '

    return Morse


def decrypt(message):
    text_message = ''
    cipher = list(message.split(' '))
    cipher = cipher[:-1]  # remove last item because it does not exist in Morse dict value

    for i in range(len(cipher)):
        message = list(Morse_CODE_DICT.keys())[list(Morse_CODE_DICT.values()).index(cipher[i])]
        text_message += message

    return text_message


def main():
    user_choice = input("Type 'E' to convert latin alphabet to Morse code.\n"
                        "Type 'D' to convert Morse code to latin alphabet.\n"
                        "(E/D?) ").upper()

    if user_choice == "E":
        message = input("Type the text: ")
        result = encrypt(message)
        print(result)
        return main()
    elif user_choice == "D":
        message = input("Type the Morse code: ")
        result = decrypt(message)
        print(result)
        return main()

    else:
        print("Wrong input.")
        return main()


if __name__ == '__main__':
    main()
