#sum of squares of first n natural numbers
def natural(x):
    sum=0
    for i in range(0,x+1):
        sum+=i**2
    print(sum)
natural(10)