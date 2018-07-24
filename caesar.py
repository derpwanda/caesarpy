from sys import argv, exit
from helpers import alphabet_position, rotate_character

def user_input_is_valid(cl_args):
    if len(cl_args) != 2:
        return False
    else:
        rot = cl_args[1]
        if rot.isdigit():
            return True
        else:
            return False

#if user_input_is_valid(argv) == False:
    #print('usage: python3 caesar.py number')
    #exit()


def encrypt(text, rot):
    encrypt_text = ''
    for x in text:
        encrypt_text = encrypt_text + rotate_character(x, rot)
    return encrypt_text

#orig_mess = input('What is your message? ')
#rot_num = int(argv[1])

#print(encrypt(orig_mess, rot_num))
