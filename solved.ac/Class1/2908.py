# 2908. 상수 (https://www.acmicpc.net/problem/2908)

a, b = map(int, input().split())

a_list = list(map(int, str(a)))
b_list = list(map(int, str(b)))

a_list[0], a_list[2] = a_list[2], a_list[0]
b_list[0], b_list[2] = b_list[2], b_list[0]

a_s = [str(i) for i in a_list]
b_s = [str(i) for i in b_list]

a = int("".join(a_s))
b = int("".join(b_s))

if (a > b):
  print(a)
else:
  print(b)