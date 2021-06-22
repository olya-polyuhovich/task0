s=input("Enter a string:") #прийняття рядку
l=[]
numbs=[]

for ch in list(s): #перенесення букв і чисел у окремі масиви
    if ch.isdigit():
        numbs.append(ch)
    else:
        l.append(ch)
        ls="".join(l)
print("String without numbers:",ls)
print("List of numbers:",numbs)

def cap(s): #застосування верхнього регістру до першої та останньої букв кожного слова (з інтернету ;) )
     s, result = s.title(), ""
     for word in s.split():
        result += word[:-1] + word[-1].upper() + " "
     return result[:-1]     
print("Capitalized first and last letters:",cap(ls))

a=max(numbs) #визначення найбільшого елемента масиву чисел
print("Max element of the number list:",a)

numbs2=[]
numbs.remove(a) #видалення найбільшого елемента з масиву
for i in range(len(numbs)): #піднесення елементів масиву до степеню по індексу
    numbs2.append(int(numbs[i])**i)
print("List of powered numbers:", numbs2)
    
