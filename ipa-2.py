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
    for i in message:
        if i == " ":
            print(" ", end="")
        else:
            letter = i
            alphabet = list('abcdefghijklmnopqrstuvwxyz')
            index = alphabet.index(letter.lower())
            shifted_index = (index + shift) % 26
            shifted_letter = alphabet[shifted_index]

            if letter.isupper():
                shifted_letter = shifted_letter.upper()
            print(shifted_letter, end="")
    return shifted_letter


messager=str(input("Put message:"))
shifty=int(input("Number of shift:"))
caesar_cipher(messager, shifty)

def shift_by_letter(letter, letter_shift):
    if letter == " ":
        print(" ")
    elif letter == "":
        print(" ")
    else:
        letter_shift = letter_shift.upper()
        letter_shift = ord(letter_shift) - 65
        alphabet = list('abcdefghijklmnopqrstuvwxyz')
        index = alphabet.index(letter.lower())
        shifted_index = (index + letter_shift) % 26
        shifted_letter = alphabet[shifted_index]

        if letter.isupper():
            shifted_letter = shifted_letter.upper()
        print(shifted_letter)
        return(shifted_letter)

liter = str(input("input a letter buddy"))
liter_ship = str(input("isa pang letter buddy"))
shift_by_letter(liter,liter_ship)

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


message = input("Ano message mo para sa madlang people? : ")
key = input("bigay ka isang word tapos dapat di siya mas mahaba sa message mo kanina ")

encrypted_text = vigenere_cipher(message, key)
print("Encrypted text:", encrypted_text)



def scytale_cipher(message, shift):
    # Prepare the grid
    ciphertext = ""
    rows = len(message) // shift
    if len(message) % shift != 0:
        rows += 1
    grid = [[""] * shift for _ in range(rows)]

    # Fill the grid with the plaintext
    char_index = 0
    for col in range(shift):
        for row in range(rows):
            if char_index < len(message):
                grid[row][col] = message[char_index]
                char_index += 1

    # Read the ciphertext column by column
    for row in range(rows):
        for col in range(shift):
            ciphertext += grid[row][col]

    return ciphertext


mensahe = input("Enter the message (scytale): ")
diameter = int(input("Enter the shift of the Scytale: "))

encrypted_text = scytale_cipher(mensahe, diameter)
print("Encrypted text:", encrypted_text)


def scytale_decipher(message, shift):
    # Prepare the grid
    plaintext = ""
    rows = len(message) // shift
    if len(message) % shift != 0:
        rows += 1
    grid = [[""] * shift for _ in range(rows)]

    # Fill the grid with the ciphertext
    char_index = 0
    for row in range(rows):
        for col in range(shift):
            if char_index < len(message):
                grid[row][col] = message[char_index]
                char_index += 1

    # Read the plaintext row by row
    for col in range(shift):
        for row in range(rows):
            plaintext += grid[row][col]

    return plaintext


text_encrypt = input("Enter the ciphertext: ")
shift = int(input("Enter the diameter of the Scytale: "))

decrypted_text = scytale_decipher(text_encrypt, shift)
print("Decrypted text:", decrypted_text)
