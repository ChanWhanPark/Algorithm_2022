# 1546. 평균 (https://www.acmicpc.net/problem/1546)

num = int(input())
array = list(map(int, input().split()))

max_val = max(array)

for idx in range(len(array)):
  array[idx] *= (100 / max_val)

print(sum(array) / num)