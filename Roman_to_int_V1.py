class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        my_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'a': 4,
            'b': 9,
            'c': 40,
            'd': 90,
            'e': 400,
            'f': 900}

        excp_dict = {
            'a': 'IV',
            'b': 'IX',
            'c': 'XL',
            'd': 'XC',
            'e': 'CD',
            'f': 'CM'
        }

        for key, value in excp_dict.items():
            s = s.replace(value, key)

        for l in s:
            result += my_dict[l]
        return result
