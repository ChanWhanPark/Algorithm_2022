# 3052. 나머지 (https://www.acmicpc.net/problem/3052)
from collections import Counter

array = []
for i in range(10):
  array.append(int(input()))
  array[i] %= 42

counter = Counter(array)
dict_count = dict(counter)
print(len(dict_count))