string = ""

num=[1,2,0,0]
k =34
d=len(str(k))
f=len(num)
while(d>0):
    num[f-1] += k%10
    k=k//10
    f-=1
    d-=1
print(num)