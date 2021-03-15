n = int(input())
stock = set(map(int, input().split()))
m = int(input())
req = list(map(int, input().split()))

for i in req:
    if i in stock:
        print('yes', end=' ')
    else:
        print('no', end=' ')

