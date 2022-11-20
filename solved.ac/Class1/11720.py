# 11720. 숫자의 합 (https://www.acmicpc.net/problem/11720)

num = int(input())
numbers = input()

sum = 0
for n in range(len(numbers)):
  sum += int(numbers[n])

print(sum)