n=int(input("Enter a number: "))
sum=0
for i in range(1,n+1):
    sum=sum+i
    print("sum is", sum)
n=int(input())
sum=0
for i in range(1,n+1):
    sum=sum+i
print("sum is",sum)
n=int(input())
for i in range(1,11):
    print(f"{n}X{i}={n*i}")
n=int(input("Enter a number: "))
if n>=0:
    product=1
for i in range(n,0,-1):
    product=product*i
else:
    product="not considered"
print(product)
num=int(input("enter the number:"))
i=1
while(i<=10):
    print(f"{num}X{i}={num*i}")
    i=i+1