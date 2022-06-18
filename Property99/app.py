stringOfnum=0
mul=1
add=0
l=[]
result=0
ans=[]

for i in range(1,10000):
    for j in str(i):
        add+=int(j)
        mul*=int(j)
        l.append((add,mul))
    result=add+mul
    if result==i:
        ans.append(i)
    add=0
    mul=1


# for a,m in l:
#     print("Add: ",a,"Mul: ",m)

print(ans)
# for j in "45":
#     add+=int(j)
#     mul*=int(j)
# print(add)
# print(mul)