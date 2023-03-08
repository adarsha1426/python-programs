#to find the factorial of a number
def factorial(x):
    if x==0 or x==1:
        return 1
    else:
        z=factorial(x-1)*x
        return z
z=factorial(5)
print(f"Factorial of 5 is {z}")