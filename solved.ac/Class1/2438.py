# 2438. 별 찍기 1 (https://www.acmicpc.net/problem/2438)

num = int(input())
for i in range(1, num + 1):
  for j in range(i):
    print("*", end="")
  print()