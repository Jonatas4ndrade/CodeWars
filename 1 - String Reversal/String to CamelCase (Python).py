def to_camel_case(text):
    
    # Returns empty string, if empty.
    if not text:
        return text
    
    # Return value is built here.
    camelCase = ""
    
    # If true, next char will be converted to uppercase.
    slashFlag = False
    
    for char in text:
        if slashFlag:
            camelCase += char.upper()
            slashFlag = False
        # If slash or underscore, set flag and continue    
        elif char == "-" or char == "_":
            slashFlag = True
        else:
            camelCase += char
    return camelCase
