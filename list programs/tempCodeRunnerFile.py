#swapping the first and last elements of the list
def swap(values):
    #swapping
    length1=length(str(values))
    temp=values[0]
    values[0]=values[length1-1]
    values[length1-1]=temp
    return values
integers=[1,23,32,123]
print(swap(integers))

#finding the length of the list
def length(unknown_list):

    count=0
    for item in unknown_list:
        count=count+1
    print(f"length of a list is {count}")
car=["mercedes","bmw","ford"]
length(car)    