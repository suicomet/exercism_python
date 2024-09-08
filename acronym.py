def abbreviate (words:str) -> str:
    new_word = ""
    for letter in words:
        if (letter == " " or letter.isalpha()):
            new_word+= letter
        elif letter == "-":
            new_word+= " "

    word_list = new_word.split(" ")
    abbr_str = ""
    for initial in word_list:
        try:
            if initial[0].isalpha():
                abbr_str += initial[0]
        except:
            IndexError
        
    
    abbr_str = abbr_str.upper()
    return abbr_str
print(abbreviate("Something - I made up from thin air"))
