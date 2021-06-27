def solution(people, limit):
    people.sort()
    cnt = 0

    left = 0
    right = len(people) - 1

    # 가벼운쪽(left)과 무거운쪽(right)에서 한명씩 뽑아 짝지으면서 가운데로 좁히기
    # 가장 가벼운 사람과도 같이 못탈 정도로 무거워야 혼자 타므로 항상 최선임
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        elif people[left] + people[right] > limit:
            right -= 1

        cnt += 1

    '''
    # 실제로 원소를 제거하게 하면 효율성 탈락임
    # 파이썬에서 원소 제거할 땐 시간복잡도를 고려하자

    while people:
        t = people.pop(0)

        for x in people:
            if t + x <= limit:
                people.remove(x)
                break

        cnt += 1
    '''

    return cnt
