#to find the fibonacci series
def fib(n):
    while n>=0:
        if  n==1 or n==0:
            return n
        else:
            return (fib(n-1)+fib(n-2))
x=10
print("The series")
for i in range(0,x):
    print(fib(i))