# 2675. 문자열 반복 (https://www.acmicpc.net/problem/2675)

T = int(input())

for _ in range(T):
  num, string = input().split()

  for i in range(len(string)):
    for j in range(int(num)):
      print(string[i], end="")

  print()