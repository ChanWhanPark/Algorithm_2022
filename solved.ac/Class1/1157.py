## 1157. 단어 공부 (https://www.acmicpc.net/problem/1157)
'''
word = input()
word = word.upper()
array = [0] * 26

for w in word:
  array[ord(w) - 65] += 1

max = 0
max_idx = 0
for idx in range(len(array)):
  if array[idx] > max:
    max = array[idx]
    max_idx = idx
  elif array[idx] == max and max != 0:
    print("?")
    break

  if idx == len(array) - 1:
    print(chr(max_idx + 65))
'''

word = input().upper()
unique_word = list(set(word))

cnt_list = []
for x in unique_word:
  cnt = word.count(x)
  cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
  print("?")
else:
  max_index = cnt_list.index(max(cnt_list))
  print(unique_word[max_index])