lst = [False, False] + [True] * 246912

for i in range(2, 123456*2+1):
  if lst[i]:
    for j in range(2*i, 123456*2+1, i):
        lst[j] = False

while True:
   n = int(input())
   if n == 0:
      break
   else:
      print(sum(lst[n+1:2*n+1]))
