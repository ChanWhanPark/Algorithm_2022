## 1152. 단어의 개수 (https://www.acmicpc.net/problem/1152)
'''
sentence = input()

idx = 0
count = 1
for s in sentence:
  if s == " " and idx != 0 and idx != len(sentence) - 1:
    count += 1
  idx += 1

if len(sentence) == 0:
  count = 0

print(count)
'''

sentence = input().split()
print(len(sentence))