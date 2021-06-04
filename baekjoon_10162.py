time = int(input())

A = time // 300
B = (time - (A * 300)) // 60
C = (time - (A*300) - (B*60)) // 10

if (time - (A*300) - (B*60) - (C*10)) != 0:
  print(-1)
else:
  print(A,B,C)
