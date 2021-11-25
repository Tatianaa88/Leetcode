def romanToInt(s):
    result = 0
    my_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }


    for index, l in enumerate(s):
        result += my_dict[l]
        if index != len(s) - 1:
            if l == 'I' and (s[index + 1] == 'V' or s[index + 1] == 'X'):
                result -= 2
            elif l == 'X' and (s[index + 1] == 'L' or s[index + 1] == 'C'):
                result -= 20
            elif l == 'C' and (s[index + 1] == 'D' or s[index + 1] == 'M'):
                result -= 200
    return result

print(romanToInt("III"))