def arith_geo (check_): 
    '''
    This is a function that checks if a list passed to it is 
    arithmetic, 
    geometric, 
    neither or 
    its empty
    '''
    if len(check_) == 0:
        return 0

    elif is_arithmetic(check_):
        return 'Arithmetic'

    elif is_geometric(check_): 
        return 'Geometric'

    else:
        return -1

def is_arithmetic(l):
    difference = l[1] - l[0]
    for index in range(len(l) - 1):
        if not (l[index + 1] - l[index] == difference):
             return False
    return True

def is_geometric(a):
    ratio = a[1]/float(a[0])
    for index in range(len(a)-1):
        if not (a[index + 1] / float(a[index]) == ratio):
            return False
    return True