# 1259. 팰린드롬수 (https://www.acmicpc.net/problem/1259)

while True:
  num = input()
  answer = 1
  if num == '0':
    break
  for i in range(len(num)):
    if num[i] != num[len(num) - 1 - i]:
      answer = 0
      break
  
  if answer == 0:
    print("no")
  else:
    print("yes")