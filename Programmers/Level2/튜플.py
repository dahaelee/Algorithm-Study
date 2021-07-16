def solution(s):
    sets = s[2:-2].split('},{')
    set_list = []

    for s in sets:
        set_list.append(list(map(int, s.split(','))))

    set_list.sort(key=len)

    answer_list = []

    for i in range(len(set_list)):
        if i == 0:
            answer_list += set_list[i]
        else:
            answer_list += [x for x in set_list[i] if x not in set_list[i - 1]]

    return answer_list
