# 2475. 검증수 (https://www.acmicpc.net/problem/2475)

array = list(map(int, input().split()))

for i in range(len(array)):
  array[i] *= array[i]

print(sum(array) % 10)