# 2920. 음계 (https://www.acmicpc.net/problem/2920)

array = list(map(int, input().split()))

flag = 0

for i in range(len(array) - 1):
  if array[i] < array[i+1]:
    flag += 1
  else:
    flag -= 1

if flag == 7:
  print("ascending")
elif flag == -7:
  print("descending")
else:
  print("mixed")