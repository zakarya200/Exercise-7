n=[]
for i in range(int(input("please entre the number:"))):
    n.append(i)
x=n[0]
for i in n:
    if i>x and i%2==0:
        x=i
print(x)