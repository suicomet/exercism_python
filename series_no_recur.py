def slices(series:str, length:int)->list[str]:
    slices_list = []
    digits_str = ""
    #exceptions 
    if length == 0:
        raise ValueError("slice length cannot be zero")
    elif length < 0:
        raise ValueError("slice length cannot be negative")
    elif series == "":
        raise ValueError("series cannot be empty")
    elif len(series) < length:
        raise ValueError("slice length cannot be greater than series length")
    
    while len(series) >= length:
        for digit in series:
            digits_str+= digit
            if len(digits_str) == length:
                slices_list.append(digits_str)
                series = series[1:]
                digits_str = ""
                break
    
    return slices_list

print(slices("918493904243", 5))