#to check the element is present in the list or not
def creating_list():
    n=int(input("Enter the number of elements in the list:"))
    values=[]
    print("\nEnter the elements in list")
    for item in range(0,n):
        item=int(input())
        values.append(item)
    print(f"The values in the list are: \n {values}")
    return values

#searching through the list
def search():
    list_1=creating_list()
    n=len(list_1)
    search_item=int(input("Enter the value to be searched:\n"))
    found=0
    for item in list_1:
            if search_item==item:
              found=1
              break
    if found:
         print("Element is Found")
    elif found==1:
         print("Not found")
search()