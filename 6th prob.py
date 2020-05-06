import math
s = int(input("enter the range"))
a = 0
b = 1
print(a,"\t",b,end="")
for i in range (1,s+1,1):
    c=a+b
    print("\t", c ,end="")
    a=b
    b=c
def isPerfectSquare(x):
   s = int(math.sqrt(x))
   return s*s == x
def isFibonacci(n):
   return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

if(isFibonacci(s) == True):
    print("\n",s,"number is a fibonnaci")
else:
    print("\n",s,"number is not fibonnaci")