#this is an example of enumerate function to use in list
characters=["Naruto" , "Luffy" , "Ichigo" , "Eren"]
for hero in enumerate(characters):
    print(hero)
#without using counter values
for count,hero in enumerate(characters,100): #here the counter starts from 100
    print(count,hero)
#to print the index:
for count,hero in enumerate(characters):
    print(count)
    print(hero)

"""
instead of using this kind of code we use enumerate 
    count = 0
    for count in characters:
        print(hero)
        count+=1
"""