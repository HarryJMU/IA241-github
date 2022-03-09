'''
lec 7
'''

#while loop

i=5
while i>=0:
    print(i)
    i=i-1
    

i= 5
while i>=0:
    i=i-1
    print (i)
    
#break statement

i = 5 
while i >=0:
    i=i-1
    if i ==3:
        break
    print(i)
    

i = 5 
while i >=0:
    i=i-1
    if i ==3:
        continue
    print(i)

i = 5 
while i >=0:
    i=i-1
    if i ==3:
        break
    print(i)
    
#pass
i = 5 
while i >=0:
    
    i=i-1
    if i ==3:
       pass
   
    print(i)
    
    
i =5

while i >=0 :
    try:
        print (1/(i-3))
    
    except:
        continue
    
    i=i-1