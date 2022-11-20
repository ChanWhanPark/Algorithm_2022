# 10809. 알파벳 찾기 (https://www.acmicpc.net/problem/10809)

word = input()
array = [-1] * 26
idx = 0
for w in word:
  num = ord(w) - 97
  if (array[num] == -1):
    array[num] = idx
  idx += 1

for a in array:
  print(a, end=" ")