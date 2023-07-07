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

