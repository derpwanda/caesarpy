def alphabet_position(letter):
     alpha = 'abcdefghijklmnopqrstuvwxyz'
     letter = letter.lower()

     return alpha.index(letter)

def rotate_character(char, rot):
    if char.isalpha(): #ignore char that are NOT letters
        rotat_posit = (alphabet_position(char) + rot) % 26 #new rotated position
        position = int(rotat_posit) + ord('a') #new rototated position + ascii 97
        if char.isupper():
            return chr(position).upper()

        else:
            return chr(position) #convert int(position) back to letter
    else:
        return char
