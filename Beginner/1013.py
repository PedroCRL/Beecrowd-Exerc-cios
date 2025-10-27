a,b,c= list(map(int,input().split()))
x=((a+b+abs(a-b))/2)
f=((x+c+abs(x-c))/2)
print("%d eh o maior"%f)