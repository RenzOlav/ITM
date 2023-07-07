'''Individual Programming Assignment 2

70 points

This assignment will develop your proficiency with Python's control flows.
'''

def shift_letter(letter, shift):
    if letter == " ":
        return " "
    elif letter == "":
        return ""
    else:
        alphabet = list('abcdefghijklmnopqrstuvwxyz')
        index = alphabet.index(letter.lower())
        shifted_index = (index + shift) % 26
        shifted_letter = alphabet[shifted_index]

        if letter.isupper():
            shifted_letter = shifted_letter.upper()
        return shifted_letter




# Example usage
input_letter = str(input("Enter a letter: "))
shift_amount = int(input("Enter the shift amount: "))
print(shift_letter(input_letter,shift_amount))

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
    return shifted_message


messager=str(input("Put message:"))
shifty=int(input("Number of shift:"))
print(caesar_cipher(messager, shifty))

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
    return ciphertext


message = input("Ano message mo?: ")
key = input("bigay ka isang word: ")
print("Encrypted text:", vigenere_cipher(message, key))


def scytale_cipher(message, shift):
    message_length = len(message)

    # Check if the length of the message is a multiple of the shift
    if message_length % shift != 0:
        # Add additional underscores to make it a multiple
        message += "_" * (shift - (message_length % shift))

    encoded_message = ""
    for i in range(message_length):
        index = (i // shift) + (message_length // shift) * (i % shift)
        encoded_message += message[index]

    return encoded_message


message = input("Enter the message: ")
shift = int(input("Enter the shift: "))

encrypted_message = scytale_cipher(message, shift)
print("Encrypted message:", encrypted_message)

def scytale_decipher(message, shift):
    # Determine the length of each rail
    rail_length = len(message) // shift

    # Create a list of empty strings to represent the rails
    rails = [''] * shift

    # Distribute the characters of the message onto the rails
    for i in range(len(message)):
        rail_index = i % shift
        rails[rail_index] += message[i]

    # Read the rails vertically to obtain the deciphered message
    deciphered_message = ''
    for rail in rails:
        deciphered_message += rail

    return deciphered_message



text_encrypt = input("Enter the ciphertext: ")
shift = int(input("Enter the diameter of the Scytale: "))

decrypted_text = scytale_decipher(text_encrypt, shift)
print("Decrypted text:", decrypted_text)
