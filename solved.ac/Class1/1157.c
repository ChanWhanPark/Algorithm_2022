// 1157. 단어 공부 (https://www.acmicpc.net/problem/1157)
#include <stdio.h>
#include <string.h>

int main()
{
  int max, result = 0, len;
  char arr[1000000];
  int alp_cnt[26] = {0, };
  int select = 0;

  scanf("%s", arr);
  len = strlen(arr);

  for (int i = 'a'; i<='z';i++){
    for (int j=0;j<len;j++){
      if (i == arr[j]) alp_cnt[i - 'a']++;
    }
  }

  for (int i='A';i<='Z';i++){
    for (int j=0;j<len;j++){
      if (i == arr[j]) alp_cnt[i - 'A']++;
    }
  }

  max = alp_cnt[0];
  for (int i=1;i<26;i++){
    if (max < alp_cnt[i]){
      max = alp_cnt[i];
      select = i;
    }
  }

  for (int i=1;i<26;i++){
    if (max == alp_cnt[i]){
      result++;
    }
  }

  if (result > 1) printf("\n");
  else printf("%c", select +'A');

  return 0;
}