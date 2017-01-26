from string import ascii_lowercase

def alphabet_position(letter):
    return ascii_lowercase.find(letter.lower())

def rotate_character(char, rot):
    temp = ascii_lowercase[(alphabet_position(char) + rot) % 26]
    if char.isupper():
        return temp.upper()
    else:
        return temp.lower()

def encrypt(text, rot):
    newText = ""
    for i in text:
        if i.isalpha():
            newText += rotate_character(i, rot)
        else:
            newText = newText + i
    return newText

def user_input_is_valid(cl_args):
     return len(cl_args) == 2 and cl_args[1].isdigit()
