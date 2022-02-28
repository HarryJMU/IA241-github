'''
lab 5
'''

#3.1
alien_color='red'

if alien_color== 'green':
    print('you have earned 5 points')
    
#3.2

if alien_color=='green':
    print('you have earned 5 points')
else:
    print('you have earned 10 points')

#3.3

favorite_fruit=['orange','apple','mango']

if 'mango' in favorite_fruit:
    print('you really like mango')
    
if 'banana' in favorite_fruit:
    print('you really like banana')
    
if 'apple' in favorite_fruit:
    print('you really like apple')
    
#3.4

age = 45

if age<10:
    print('kid')
    
if age <20:
    print('teenager')

elif age>=20 and age <20:
    print('teenager')
    
else:
    print('adult')
    
if age >=60:
    print('elder')