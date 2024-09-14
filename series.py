def slices(series:str, length:int) -> list[str]:

    digits_str = ""
    #exceptions 
    if length == 0:
        raise ValueError("slice length cannot be zero")
    elif length < 0:
        raise ValueError("slice length cannot be negative")
    elif series == "":
        raise ValueError("series cannot be empty")





    if len(series) < length:
        return slices_list


    slices_list = []
    for digit in series:
        digits_str+= digit
        if len(digits_str) == length:

            slices_list.append(digits_str)
            series = series[1:]
            return slices_list + slices(series, length)

        

#slices("918493904243", 5) -> ["91849", "18493", "84939", "49390", "93904", "39042", "90424", "04243"]

print(slices("918493904243", 5))