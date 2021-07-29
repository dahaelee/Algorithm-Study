import math


def split(str):
    str = str.lower()
    l = []

    for i in range(len(str) - 1):
        tmp = str[i:i + 2]
        if tmp.isalpha():
            l.append(tmp)

    return l


def solution(str1, str2):
    list1, list2 = split(str1), split(str2)

    if not list1 and not list2:
        return 65536

    set1, set2 = set(list1), set(list2)
    inter = set1 & set2
    union = set1 | set2

    inter_cnt = len(inter)
    union_cnt = len(union)

    for x in inter:
        inter_cnt += (min(list1.count(x), list2.count(x)) - 1)

    for x in union:
        union_cnt += (max(list1.count(x), list2.count(x)) - 1)

    return math.floor(inter_cnt / union_cnt * 65536)
