def alphabet_position(char):
    if char == char.lower():
        return ord(char) - 97
    elif char == char.upper():
        return ord(char) - 65
    else:
        return char

def rotate_character(char, rot):
    for char in char:
        if char == char.lower():
            return chr((alphabet_position(char) + rot) % 26 + 97)
        elif char == char.upper():
            return chr((alphabet_position(char) + rot) % 26 + 65)
        else:
            return char

def encrypt(plaintext, rot):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha() == True:
            ciphertext += rotate_character(char, rot)
        else:
            ciphertext += char
    return ciphertext
