def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    for char in str_number:
        if char == '0':
            str_number += '1'
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    elif len(str_number) == 1:
        return first


result = get_multiplied_digits(40203)
print(result)