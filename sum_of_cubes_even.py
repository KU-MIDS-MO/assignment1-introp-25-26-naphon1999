def sum_of_cubes_even(n):
    ### Replace with your own code (begin) ###
    sum = 0

    if n < 0:
        return -1
    if type(n) != int:
        return -1
    if n > 2000:
        print("a warning but still compute")

    for i in range(0,n+1):
        if n > 0 and i%2 == 0:
            sum += i**3
    return float(sum)
