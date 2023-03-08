#Maximum of two numbers in Python
def maximum_number(array):
    n=len(array)
    if n==0:
        print(f"the array is empty")
    maximum=array[0]
    for item in range(1,n-1):
        if array[item]<array[item+1]:
            maximum=array[item+1]
    print(f"The maximum number in the array is {maximum}")
x=[10,22,45,122]
maximum_number(x)
