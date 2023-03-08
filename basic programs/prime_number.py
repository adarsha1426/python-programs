def prime(x):
    for i in range(2,x):
        if x%i==0:
            print("The given number is not prime number")
            break
    else:
        print("The given number is prime")
prime(19)