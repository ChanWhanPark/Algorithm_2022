# 2884. ěë ěęł (https://www.acmicpc.net/problem/2884)

h, m = map(int, input().split())

m -= 45

if (m < 0):
  h -= 1
  if (h < 0):
    h += 24
  m += 60

print(h, m)