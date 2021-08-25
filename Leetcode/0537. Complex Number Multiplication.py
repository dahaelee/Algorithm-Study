class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def get_parts(num):
            num_splitted = num.split('+')
            r, i = int(num_splitted[0]), int(num_splitted[1][:-1])
            return r, i

        r1, i1 = get_parts(num1)
        r2, i2 = get_parts(num2)

        return str(r1 * r2 - i1 * i2) + '+' + str(r1 * i2 + i1 * r2) + 'i'
