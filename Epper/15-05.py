def solution(string):
    chars = []

    if string[0] == 1:
        chars.append('1')

    cnt = 0
    for i in range(len(string)-1):
        if string[i] != string[i+1]:
            chars.append(chr(ord('A') + cnt))
            cnt = 0
        else:
            cnt += 1
    chars.append(chr(ord('A') + cnt))

    result = ''.join(chars)
    return result

string = input()
result = solution(string)
print(result)
