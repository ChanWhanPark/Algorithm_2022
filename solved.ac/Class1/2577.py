# 2577. 숫자의 개수 (https://www.acmicpc.net/problem/2577)

a = int(input())
b = int(input())
c = int(input())

mul = a * b * c
mul_list = list(map(int, str(mul)))
array = [0] * 10

for m in mul_list:
  for i in range(len(array)):
    if m == i:
      array[i] += 1

for i in range(len(array)):
  print(array[i])