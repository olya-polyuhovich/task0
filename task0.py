import random as r
list=[r.randint(-100,100) for i in range (30)] #створення списку
print(list)
print("\nMax element:",max(list)) #пошук максимального елемента
print("\nPosition of the max element:",list.index(max(list))) #визначення індексу максимального елемента
print("\nPares of neg elements:")
for i in range (len(list)): #пошук пар від'ємних чисел
    if list[i]<0 and list[i+1]<0:
        print(list[i],list[i+1],sep=",")
