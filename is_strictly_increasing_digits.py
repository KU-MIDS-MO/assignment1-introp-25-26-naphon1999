def is_strictly_increasing_digits(n):
    ### Replace with your own code (begin) ###
    a = str(n)
    
    if type(n) != int or int(n) < 0:
        return -1

    for i in range(len(a)-1):
        if int(a[i]) >= int(a[i+1]):
            return False
    return True