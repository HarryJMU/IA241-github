'''
lec 5
if statement
'''

import this 

#White Spacing Formatting

print (1+ 
2   )
print([1,2,3,
        4,5,6])
m=1\
+2

print (m)

#is Operator 

a=[1,2,3]
b=[1,2,3]

print (id([1,2,3]))
print(id(a))
print(id(b))

print(a is b)
print (a==b)

#None

x = None

print(id(None))
print(id(x))

print(x==None)
print((x is None))

y = []
print(y==None)
print(y is None)

#Boolean type

print (True and False)
print (True or False)

print (not True)
print (not False)

print (not None)
print (not '0')
print( not "") #"" means 'empty = false'
print( not "0") #string=true

print(() and [])

print (-1 or 0) #only 0 is considered false
print (0 or -1)

#if statement

if 2>1: 
    print('2>1')
    if 3>1:
        print('3>1')
        
    if 2<=1:
        print('2<=1')
    
print('not in the if block')

#if else

if 2>=1:
    print('2>=1')
else:
    print('2<1')
    
#if-elif-else chain

if 2<=1:
    print('2<=1')
elif 2<=2:
    print('2<=2')
else:
    print('2>1')
    
