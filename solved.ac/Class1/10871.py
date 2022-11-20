# 10871. X보다 작은 수 (https://www.acmicpc.net/problem/10871)

n, x = map(int, input().split())
array = list(map(int, input().split()))

for a in array:
  if a < x:
    print(a, end=" ")