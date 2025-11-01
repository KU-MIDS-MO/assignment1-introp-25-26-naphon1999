def count_digits_greater_than(n, t):
    ### Replace with your own code (begin) ###
    a = str(n)
    count = 0

    if int(n) < 0:
        return -1
    if type(t) != int:
        return -1
    if t < 0 or t > 9:
        return -1
    
    for i in a:
        if int(n) >= 0 and 0 <= int(t) <= 9 and int(i) > t:
            count += 1
    return count

