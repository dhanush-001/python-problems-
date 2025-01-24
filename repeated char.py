def repeated_char(s):
    seen = set()

    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return none

print(repeated_char("dhanush"))
        
