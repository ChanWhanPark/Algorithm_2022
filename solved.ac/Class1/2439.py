# 2439. 별 찍기 2 (https://www.acmicpc.net/problem/2439)
num = int(input())
for i in range(1, num+1):
  for j in range(i, num):
    print(" ", end="")
  for k in range(i):
    print("*", end="")
  print()