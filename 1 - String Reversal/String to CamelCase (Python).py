def to_camel_case(text):
    # Returns empty string.
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
        elif char == "-" or char == "_":
            slashFlag = True
        else:
            camelCase += char
    return camelCase