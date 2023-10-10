import math

n,d,p= [int(x) for x in input().split()]
F = [int(x) for x in input().split()]

ans=int()

# 降順
F.sort(reverse=True)

for i in range(0,len(F),d):
  t = 0
  for j in range(d):
    if len(F) < i+j+1:
      break
    t += F[i+j]
  if p < t:
    ans += p
  else:
    ans += sum(F[i:])
    break

print(ans)