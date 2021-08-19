class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        if s == '0':
            return 0
        if n == 1:
            return 1

        # 두 자리 이상의 s에 대해서만 dp
        d = [0] * (n + 1)
        d[0] = 1
        d[1] = 1 if s[0] != '0' else 0

        for i in range(2, n + 1):
            if s[i - 1] != '0':  # 한자리 확인
                d[i] += d[i - 1]
            if 10 <= int(s[i - 2:i]) <= 26:  # 두자리 확인
                d[i] += d[i - 2]

        return d[n]
