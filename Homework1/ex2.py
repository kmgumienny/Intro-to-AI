def isreverse(s1, s2):
    # Your code here

    #check if both strings are completely processed
    if len(s1) == 0 and len(s2) == 0:
        return True

    #if the strings are of unequal length, return false
    elif len(s1) != len(s2):
        return False

    #checks the first char of s1 against the last char of s2
    elif s1[0] != s2[-1]:
        return False
    else:
        return isreverse(s1[1:], s2[:-1])


