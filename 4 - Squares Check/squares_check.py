from collections import defaultdict

def comp(array1, array2):

    if array1 is None or array2 is None:
        return False

    # Dictionaries were used as they are implemented using hash tables
    # and don't need to be sorted for comparison
    # Check documention on dict_equal(PyDictObject *a, PyDictObject *b) function. 
    dic1 = defaultdict(int)
    dic2 = defaultdict(int)
    
    for value in array1:
        dic1[value ** 2] += 1
        
    for value in array2:
        dic2[value] += 1

    return dic1 == dic2
