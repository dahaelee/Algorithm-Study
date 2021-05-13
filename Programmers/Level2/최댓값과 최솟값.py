def solution(s):
    nums = [int(x) for x in s.split(' ')]
    return f"{str(min(nums))} {str(max(nums))}"
