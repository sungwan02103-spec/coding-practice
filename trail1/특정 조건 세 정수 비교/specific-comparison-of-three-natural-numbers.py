a, b, c = map(int,input().split())
m = min(a,b,c)

print(1 if a==m else 0, end=" ")
print(1 if a==b==c else 0, end=" " )