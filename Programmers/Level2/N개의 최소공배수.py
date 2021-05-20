def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def solution(arr):
    answer = arr[0]

    for x in arr:
        answer = answer * x / gcd(answer, x)

    return answer


'''
def gcd(a, b):
    while b > 0:
        a, b = b, a % b 
    return a

def lcm(a,b):
    return a * b / gcd(a, b)

def solution(arr):

    if len(arr) == 1:
        return(arr[0])

    else: 
        d = [0] * len(arr)
        d[1] = lcm(arr[0], arr[1])

        for i in range(2, len(arr)):
            d[i] = lcm(d[i-1], arr[i])

        return d[-1]
'''
