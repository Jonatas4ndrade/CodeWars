function toCamelCase(str){
  
    var returned = ""
    var isNextUpper = false;
    
    for (i = 0; i < str.length; i++) {
        // if char is _ or - , set the flag and continue.  
        if ("-_-".includes(str[i])) {
            isNextUpper = true;
        // if the flag is set, concatenate the uppercased character.
        } else if (isNextUpper){
            returned += str[i].toUpperCase()
            isNextUpper = false;
        // if flag is false, concatenate the char as is.
        } else {
          returned += str[i];
        } 
    }
    return returned; 
  }