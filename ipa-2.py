
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

def shift_by_letter(letter, letter_shift):
    if letter == " ":
        return " "
    elif letter == "":
        return ""
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

def vigenere_cipher(message, key):
    ciphertext = ""
    key_length = len(key)
    key = key.upper()  # Convert the key to uppercase for consistency

    for i in range(len(message)):
        letter = message[i]
        if letter.isalpha():
            key_letter = key[i % key_length]
            key_shift = ord(key_letter) - 65

            if letter.isupper():
                base = 65
            else:
                base = 97

            shifted_letter = chr((ord(letter) - base + key_shift) % 26 + base)  # Apply the Vigenere cipher shift

            ciphertext += shifted_letter
        else:
            ciphertext += letter

    return ciphertext

def scytale_cipher(message, shift):
    message_length = len(message)

    while message_length % shift != 0:
        message = str(message) + ("_")
        message_length += 1

    encoded_message = ""
    for i in range(message_length):
        index = (i // shift) + (message_length // shift) * (i % shift)
        encoded_message += message[index]

    return encoded_message


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
