# min 함수 사용

n, m = map(int, input().split())

mins = []

for _ in range(n):
    row = list(map(int, input().split()))
    mins.append(min(row))

ans = max(mins)

print(ans)

# 나는 각 행의 min값 리스트를 만들어 거기서 max값을 구했는데,
# 전역변수 ans=0으로 설정하고, for문 내에서 max(ans,행의min값) 으로 max값을 갱신시켜나가는 방법도...