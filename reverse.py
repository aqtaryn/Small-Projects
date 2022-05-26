def reverse(f_any):
    f_str = str(f_any)
    new = ''
    for i in range(len(f_str)):
        new = str(f_str[i]) + new

    return new
