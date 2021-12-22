#1

x=['The wolking dead','The Sopranos','The waild west world','Beauties']
for i in (x):
        print(i)
#2
        
for i in range(25,51):
    print(i)
#3
    
shows=['The wolking dead','The Sopranos','The waild west world','Beauties']
for index, show in enumerate(shows):
   print(index)
   print(shows)
#4
   
#numbers = [11, 32, 33, 15, 1]
#while True:
#   answer = input("Guess a number or type q to quit.")
#    if answer == "q":
#        break
#    try:
#        answer = int(answer)
#    except ValueError:
#        print("please type a number or q to quit.")
#    if answer in numbers:
#        print("You guessed correctly!")
#    else:
#        print("You guessed incorrectly!")

#5

x=[8,19,148,4]
y=[9,1,33,83]
added=[]
for i in x:
     for j in y:
         added.append(i*j)
print(added)
