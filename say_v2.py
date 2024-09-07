def say(number:int) -> str:
    if number < 0 or len(str(number)) > 12:
        raise ValueError("input out of range")
    number = (str(number))[::-1]
    sep_count = 0
    sep_limit = 0  #variable to not put an extra hyphen
    str_number_total = ""
    number_len = len(number)
    for sep in number:
        sep_limit+= 1
        sep_count+= 1
        str_number_total+= sep
        if sep_count == 3 and sep_limit != number_len:
            str_number_total+= "_"
            sep_count = 0
    str_number_total = str_number_total[::-1]
    str_number_sum = ""
    str_number_final = ""
    final_list = []
    dict_below_20 = {
        1 : ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"],
        2 : ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    }

    dict_below_100 = {
        2: ["dummy_1", "dummy_2", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"],
        3: "hundred"
    }

    dict_upper_1000 = {
        2: "thousand",
        3: "million",
        4: "billion"
    }
    num_parts_list = str_number_total.split("_")
    def n_below_20 (n:str, str_number_sum:str): #"15"

        if len(n) == 2:
            str_number_sum+= dict_below_20[len(n)][int(n[1])]
        
        elif n == "000":
            str_number_sum+= ""
        

        else:
            n = int(n)
            n = str(n) 
            str_number_sum+= dict_below_20[len(n)][int(n)]
        
        return str_number_sum
    
    def n_above_20_below_100 (n:str, str_number_sum:str): #"45"
       str_number_sum+= dict_below_100[len(n)][int(n[0])]

       return str_number_sum
    
    def n_above_100_below_1000 (n:str, str_number_sum:str): #100
        str_number_sum+= dict_below_20[1][int(n[0])] + " " + "hundred" + " "

        return str_number_sum
    
    for str_number in num_parts_list:
        while str_number != "":
            if int(str_number) < 20:
                str_number_final+= n_below_20(str_number, str_number_sum)

            
            elif 20 <=int(str_number) < 100:
                if len(str_number) == 2 and str_number[-1] != "0":
                    str_number_final+= n_above_20_below_100(str_number, str_number_sum) + "-"
                else:
                    str_number_final+= n_above_20_below_100(str_number, str_number_sum)

            elif 100 <= int(str_number) <= 999:
                str_number_final += n_above_100_below_1000(str_number, str_number_sum)

            
            #eliminate the zeroes in the middle
            if len(str_number) == 2 and str_number[-1] == "0":
                break
            if int(str_number) <= 20 or str_number[1:] == "00":
                break
            str_number = str_number[1:]
            if len(str_number) == 0:
                break

            str_number = int(str_number)
            str_number = str(str_number)
            
            
        final_list.append(str_number_final)
        str_number_final = ""
    


    len_elements = len(final_list) + 1
    dict_selection = len_elements - 1
    index_append = 0
    if len(final_list) > 1:
        while len_elements:
            
            index_append+= 1
            if index_append % 2 != 0:
                try:
                    if final_list[index_append] == "":
                        final_list.insert(index_append, dict_upper_1000[dict_selection])
                    else:
                        final_list.insert(index_append, dict_upper_1000[dict_selection])
                except:
                    IndexError
                dict_selection-=1
                if final_list[-1] == "":
                    break
            len_elements-= 1
    xd = (" ".join(final_list)).strip()
    return xd

print(say(123007800))