n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

# 최대 k번. k번 다 바꿔도 되고 덜 바꿔도 됨
for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    # 같은 인덱스에서 a의 원소가 b의 원소보다 크거나 같으면 중단
    # a는 커지게, b는 작아지게 정렬돼있어서 한번 a가 역전하면 그 뒤로도 계속 a가 b보다 큼
    else :
        break

print(sum(a))
