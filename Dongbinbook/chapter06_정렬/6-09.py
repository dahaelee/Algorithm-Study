# key 값으로는 하나의 함수가 들어가야 하며 이는 정렬 기준이 됨

array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)

# key 설정에서 람다 함수를 사용하는 방법
# lambda 매개변수: 반환값
result_lambda = sorted(array, key=lambda x: x[1])
print(result_lambda)