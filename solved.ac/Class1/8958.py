# 8958. 나머지 (https://www.acmicpc.net/problem/8958)

T = int(input())

for _ in range(T):
  ans = input()

  correct = 0
  score = 0

  for a in ans:
    if a == 'O':
      correct += 1
      score += correct
    else:
      correct = 0

  print(score)

