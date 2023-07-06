'''Individual Programming Assignment 2

70 points

This assignment will develop your proficiency with Python's control flows.
'''

def shift_letter(letter, shift):
    if letter == " ":
        print(" ")
    elif letter == "":
        print(" ")
    else:
        alphabet = list('abcdefghijklmnopqrstuvwxyz')
        index = alphabet.index(letter.lower())
        shifted_index = (index + shift) % 26
        shifted_letter = alphabet[shifted_index]

        if letter.isupper():
            shifted_letter = shifted_letter.upper()
        print(shifted_letter)
        return(shifted_letter)




# Example usage
input_letter = str(input("Enter a letter: "))
shift_amount = int(input("Enter the shift amount: "))
shift_letter(input_letter,shift_amount)

def caesar_cipher(message, shift):
    shifted_message = ""  # Variable to store the shifted message

    for i in message:
        if i == " ":
            shifted_message += " "
        else:
            letter = i
            alphabet = list('abcdefghijklmnopqrstuvwxyz')
            index = alphabet.index(letter.lower())
            shifted_index = (index + shift) % 26
            shifted_letter = alphabet[shifted_index]

            if letter.isupper():
                shifted_letter = shifted_letter.upper()
            shifted_message += shifted_letter

    print(shifted_message)
    return shifted_message


messager=str(input("Put message:"))
shifty=int(input("Number of shift:"))
caesar_cipher(messager, shifty)

def shift_by_letter(letter, letter_shift):
    if letter == " ":
        return " "
    elif letter == "":
        return " "
    else:
        letter_shift = letter_shift.upper()
        letter_shift = ord(letter_shift) - 65
        alphabet = list('abcdefghijklmnopqrstuvwxyz')
        index = alphabet.index(letter.lower())
        shifted_index = (index + letter_shift) % 26
        shifted_letter = alphabet[shifted_index]

        if letter.isupper():
            shifted_letter = shifted_letter.upper()

        return shifted_letter

liter = str(input("input a letter buddy: "))
liter_ship = str(input("isa pang letter buddy: "))
result = shift_by_letter(liter, liter_ship)
print(result)


def vigenere_cipher(message, key):
    ciphertext = ""
    key_length = len(key)
    key_index = 0

    for letter in message:
        if letter.isalpha():
            letter_shift = key[key_index].upper()
            letter_shift = ord(letter_shift) - 65
            alphabet = list('abcdefghijklmnopqrstuvwxyz')
            index = alphabet.index(letter.lower())
            shifted_index = (index + letter_shift) % 26
            shifted_letter = alphabet[shifted_index]

            if letter.isupper():
                shifted_letter = shifted_letter.upper()

            ciphertext += shifted_letter
            key_index = (key_index + 1) % key_length

        else:
            ciphertext += letter

    print(ciphertext)
    return ciphertext


message = input("Ano message mo para sa madlang people? : ")
key = input("bigay ka isang word tapos dapat di siya mas mahaba sa message mo kanina ")

encrypted_text = vigenere_cipher(message, key)
print("Encrypted text:", encrypted_text)


def scytale_encrypt(message, shift):
    encoded_message = ""
    message_length = len(message)

    for i in range(message_length):
        index = (i // shift) + (message_length // shift) * (i % shift)
        encoded_message += message[index]

    return encoded_message


# Example usage
raw_message = str(input("Message"))
shift_value = int(input("shift"))
encrypted_message = scytale_encrypt(raw_message, shift_value)
print("Encrypted Message:", encrypted_message)


def scytale_decipher(message, shift):
    decoded_message = ""
    message_length = len(message)

    for i in range(message_length):
        index = (i // shift) + (message_length // shift) * (i % shift)
        decoded_message += message[index]

    return decoded_message



text_encrypt = input("Enter the ciphertext: ")
shift = int(input("Enter the diameter of the Scytale: "))

decrypted_text = scytale_decipher(text_encrypt, shift)
print("Decrypted text:", decrypted_text)
