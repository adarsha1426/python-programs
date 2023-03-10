#swapping the first and last elements of the list
def swap(values):
    #swapping
    length=int(len(values))
    temp=values[0]
    values[0]=values[length-1]
    values[length-1]=temp
    return values
integers=[1,23,32,123]
print(swap(integers))

#finding the length of the list
def length(unknown_list):
    count=0
    for item in unknown_list:
        count=count+1
    return count    
car=["mercedes","bmw","ford"]
print(length(car))    