def solution(nums):
    n = len(nums) // 2
    t = len(list(set(nums)))

    # 가져갈 수 있는 개수가 종류 수보다 많으면 종류별로, 적거나 같으면 가져갈 수 있는 개수만큼
    return t if n > t else n
