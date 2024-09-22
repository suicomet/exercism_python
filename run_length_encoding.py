def decode (string:str) -> str:
    letter_list = []
    mult_list = []
    letter_mult = ""
    for char in string:
        if char.isnumeric():
            if len(mult_list) >=1:
                mult_list.append(char)
                mult_list = ["".join(mult_list)]
            else:
                mult_list.append(char)
        elif char.isalpha() or char == " ":
            if len(mult_list) == 0:
                letter_mult += char
            else:
                mult_list.append(char)
                if len(mult_list) == 2:
                    letter_mult += int(mult_list[0]) * mult_list[1]
                    mult_list.clear()
    
    letter_list.append(letter_mult)
    letter_list = "".join(letter_list)
    return letter_list

def encode(string:str) -> str:
    len_string = len(string)
    single_letter = ""
    num_letters = 0
    final_list = []
    count_letters = ""
    mult_letters = ""
    for char in string:
        num_letters+= 1
        if len(single_letter) >= 1:
            if char == single_letter[0]:
                single_letter+= char
        
        if len(single_letter) < 1:
            single_letter= char

        if char != single_letter[0]:
            if len(single_letter) > 1:
                count_letters = str(len(single_letter))
                mult_letters = count_letters + single_letter[0]
                final_list.append(mult_letters)
                single_letter = ""
            if len(single_letter) != 0:
                final_list.append(single_letter)
            single_letter = char

        if num_letters == len_string:
            if len(single_letter) == 1:
                final_list.append(single_letter)
            else:
                count_letters = str(len(single_letter))
                mult_letters = count_letters + single_letter[0]
                final_list.append(mult_letters)
    
    final_list = "".join(final_list)
    return final_list

print(decode("12WB12W3B24WB"))
#print(encode("XYZ"))

#(decode("2A3B4C"), "AABBBCCCC")
#(encode("WDAABBBCCCC"), "WD2A3B4C")