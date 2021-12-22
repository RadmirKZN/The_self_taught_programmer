#1
import csv
with open('chalenges_files1', 'w') as f:
	w=csv.writer(f,delimiter=',')
	w.writerow(['one','two','three'])
with open('chalenges_files1', 'r') as f:
    print(f.read())

#2

answer=input('What is you name?')
with open('chalenges_files1', 'w') as f:
    f.write(answer)
#3
import csv
with open('chalenges_files1', 'w') as f:
	w=csv.writer(f,delimiter=',')
	w.writerow(['Звёздные войны','Терминатор','Искуственный интелект'])
	w.writerow(['Люди в чёрном','Я-робот','Эволюция'])
	w.writerow(['Дурак','Матильда','Левифан'])
	
 


    

