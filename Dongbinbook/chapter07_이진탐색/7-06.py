n = int(input())
stock = list(map(int, input().split()))
m = int(input())
req = list(map(int, input().split()))

array = [0] * 1000001
for i in stock:
    array[i] = 1

for i in req:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')
