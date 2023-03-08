#To check whether the given number is armstrong number or not
def armstrong(x):
    copy=x
    n=len(str(x))
    sum=0
    while x>0:
        digit=x%10
        sum=sum+digit**n
        x=x//10 #this is the integer division as "/" returns the decimal values whereas "//" retrun only interger value
    if copy==sum:
        print(f" {copy} is armstrong number. ")
    else:
        print(f"{copy} is not armstrong number. ")
armstrong(371)