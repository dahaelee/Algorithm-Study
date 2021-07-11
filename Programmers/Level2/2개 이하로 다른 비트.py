def solution(numbers):
    answer = []

    for num in numbers:
        if num % 2 == 0:
            answer.append(num + 1)
        else:
            bits = ['0'] + list(bin(num)[2:])
            cnt = 0  # 뒤에서 첫번째 0이 나올때까지 1의 개수

            for i in reversed(range(len(bits))):
                if bits[i] == '0':  # 뒤에서 첫번째 0
                    bits[i] = '1'
                    break
                else:
                    bits[i] = '0'
                    cnt += 1

            if cnt > 1:
                bits = bits[:-(cnt - 1)] + ['1'] * (cnt - 1)

            answer.append(int(''.join(bits), 2))

    return answer
