n=int(input("Enter a number-"))
if n>=2:
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        print("Prime")
    else:
        print("Not Prime")
else:
    print ("Not Prime")
n=int(input("Enter a number: "))
product=1
for i in range(n,0,-1):
    product=product*i
print(product)
