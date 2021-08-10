class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        left_one = 0
        right_zero = s.count('0')
        min_flip = right_zero

        # 플립 횟수 : 왼쪽 1->0, 오른쪽 0->1
        for x in s:
            if x == '1':
                left_one += 1
            else:
                right_zero -= 1

            min_flip = min(left_one + right_zero, min_flip)

        return min_flip
