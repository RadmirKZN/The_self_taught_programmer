#1
author='Чехов'
print(author[0])
print(author[1])
print(author[2])
print(author[3])
print(author[4])

#2

#answer1=input('Что ты вчера написал?')
#answer2=input('Куда ты вчера ходил?')
#new_string='Вчера я написал {}. Вчера я ходил {}.'.format(answer1,answer2)
#print(new_string)

#3

x='олдос Хаксли родился в 1894 году.'.capitalize()
print(x)

#4

s= 'Что это? Кто это? Когда это?'.split('?')
print(s)

#5
лиса=['Рыжая','лиса','перепрыгнула','через','низкий','забор','.']
лиса=' '.join(лиса)
лиса=лиса[0:-2]+'.'
print(лиса)

#6

f='Ребёнок зеркало поступков родителей.'
f=f.replace('о','0')
print(f)

#7

j='Хумингуэй'.index('м')
print(j)

#9

p='три'+'три'+'три'
o='три'*3
print(p)
print(o)

#10
a='И незачем так орать!Я и в первый раз прекрасно слышал.'
a=a[0:19]
print(a)
