lower = int(input("enter the low range"))
upper = int(input("enter the upper range"))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
count = 0
n = int(input("Enter a number"))
for i in range(1,n+1,1):
    if(n % i ==0):
        count += 1
if (count==2):
    print(n," is prime")
else:
    print(n,"is not prime")