def say(number:int) -> str:
    number = (str(number))[::-1]
    sep_count = 0
    str_number = ""
    for sep in number:
        sep_count+= 1
        str_number+= sep
        if sep_count == 3:
            str_number+= "_"
            sep_count = 0
    str_number = str_number[::-1]
    mag_dict = {
        1 : ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"],
        2 : ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"],
            }

    mag_sub_big_dict = { #len_digits_group
        2: ["dummy_1", "dummy_2", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"],
        3: "hundred"
    }

    mag_big_dict = { #the key signify the numbers of elements of num_list
        1 : "hundred",
        2 : "thousand",
        3 : "million",
        4 : "billion",
        5 : "stop"
        
    }
    final_str_number = ""
    num_list = str_number.split("_")
    mag_big_len = len(num_list) #number of elements inside the list
    if mag_big_len >= 5 or str_number[0] == "-": #upper than 5 is trillion
        raise ValueError("input out of range")
    mag_digits = 0
    len_digits_group = 0 # this will relate with the word on mag_dict  
    digit_index = None
    for big_num in num_list:
        #print(big_num)
        len_digits_group = len(big_num)
        
        for digit in big_num:
            #print(f"{digit}, digit")
            digit_index = big_num.index(digit) 

            if mag_big_len == 4:
                if digit_index == 0:
                    final_str_number += mag_dict[1][int(digit)] + " "
                    final_str_number += mag_sub_big_dict[len_digits_group] + " "
                    len_digits_group-= 1
                elif digit_index == 1:
                        final_str_number+= mag_sub_big_dict[len_digits_group][int(digit)] + "-"
                elif digit_index == 2:
                            final_str_number+= mag_dict[1][int(digit)] + " "
                            final_str_number+= mag_big_dict[mag_big_len] + " "
            
            if mag_big_len == 3:
                if digit_index == 0:
                    final_str_number+= mag_dict[1][int(digit)] + " "
                    final_str_number+= mag_sub_big_dict[len_digits_group] + " "
                    len_digits_group-=1
                elif digit_index == 1:
                     final_str_number+= mag_sub_big_dict[len_digits_group][int(digit)] + "-"
                elif digit_index == 2:
                    final_str_number+= mag_dict[1][int(digit)] + " "
                    final_str_number+= mag_big_dict[mag_big_len] + " "

            if mag_big_len == 2:
                if digit_index == 0:
                    final_str_number+= mag_dict[1][int(digit)] + " "
                    final_str_number+= mag_sub_big_dict[len_digits_group] + " "
                    len_digits_group-=1
                elif digit_index == 1:
                     final_str_number+= mag_sub_big_dict[len_digits_group][int(digit)] + "-"
                elif digit_index == 2:
                    final_str_number+= mag_dict[1][int(digit)] + " "
                    final_str_number+= mag_big_dict[mag_big_len] + " "
            




            if mag_big_len == 1 and len_digits_group == 2:
                if int(digit) == 0:
                     break
                if int(big_num) >= 20:
                    final_str_number+= mag_sub_big_dict[len_digits_group][int(digit)] + "-"
                    len_digits_group-= 1
                    if digit_index == 1:
                         final_str_number+= mag_dict[len_digits_group][int(digit)]
                else:
                    final_str_number+= mag_dict[len_digits_group][int(big_num[1])]

            if mag_big_len == 1 and len_digits_group != 2:
                if digit_index == 0:
                    final_str_number+= mag_dict[1][int(digit)] + " "
                    if len_digits_group > 1:
                        final_str_number+= mag_sub_big_dict[len_digits_group] + " "
                        len_digits_group-=1
                elif digit_index == 1:
                     final_str_number+= mag_sub_big_dict[len_digits_group][int(digit)] + "-"
                elif digit_index == 2:
                    final_str_number+= mag_dict[1][int(digit)] + " "
            
        mag_big_len-= 1

    final_str_number = final_str_number.strip()
    
    return final_str_number



    

print(say(20))
