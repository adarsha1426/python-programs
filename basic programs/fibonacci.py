#To find the n-th fibonacci number
def fibonacci(n):
    while n>0:
     if n==0 or n==1:
         return 1
     else:
         return n+fibonacci(n-1)
z=fibonacci(4)
print(z)