class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # You must also not convert the inputs to integers directly.
        # return str(int(num1) + int(num2))

        def str_to_num(string):
            num = 0
            digits = list(string)
            for i, digit in enumerate(digits):
                num += (ord(digit) - ord('0')) * 10 ** (len(digits) - 1 - i)
            return num

        res = str_to_num(num1) + str_to_num(num2)
        return str(res)
