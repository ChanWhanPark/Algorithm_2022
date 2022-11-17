# 2739. 구구단 (https://www.acmicpc.net/problem/2739)

num = int(input())

for i in range(1, 10):
  print(str(num) + " * " + str(i) + " = " + str(num * i))