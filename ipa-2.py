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
    '''Vigenere Cipher.
    15 points.

    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    pass

def scytale_cipher(message, shift):
    '''Scytale Cipher.
    15 points.

    Encrypts a message by simulating a scytale cipher.

    A scytale is a cylinder around which you can wrap a long strip of
        parchment that contained a string of apparent gibberish. The parchment,
        when read using the scytale, would reveal a message due to every nth
        letter now appearing next to each other, revealing a proper message.
    This encryption method is obsolete and should never be used to encrypt
        data in production settings.

    You may read more about the method here:
        https://en.wikipedia.org/wiki/Scytale

    You may follow this algorithm to implement a scytale-style cipher:
    1. Take a message to be encoded and a "shift" number.
        For this example, we will use "INFORMATION_AGE" as
        the message and 3 as the shift.
    2. Check if the length of the message is a multiple of
        the shift. If it is not, add additional underscores
        to the end of the message until it is.
        In this example, "INFORMATION_AGE" is already a multiple of 3,
        so we will leave it alone.
    3. This is the tricky part. Construct the encoded message.
        For each index i in the encoded message, use the character at the index
        (i // shift) + (len(message) // shift) * (i % shift) of the raw message.
        If this number doesn't make sense, you can play around with the cipher at
         https://dencode.com/en/cipher/scytale to try to understand it.
    4. Return the encoded message. In this case,
        the output should be "IMNNA_FTAOIGROE".

    Example:
    scytale_cipher("INFORMATION_AGE", 3) -> "IMNNA_FTAOIGROE"
    scytale_cipher("INFORMATION_AGE", 4) -> "IRIANMOGFANEOT__"
    scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8) -> "AOTSRIOALRH_EMRNGIMA_PTT"

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the encoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    pass

def scytale_decipher(message, shift):
    '''Scytale De-cipher.
    15 points.

    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.

    Example:
    scytale_decipher("IMNNA_FTAOIGROE", 3) -> "INFORMATION_AGE"
    scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8) -> "ALGORITHMS_ARE_IMPORTANT"
    scytale_decipher("IRIANMOGFANEOT__", 4) -> "INFORMATION_AGE_"

    There is no further brief for this number.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the decoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    pass