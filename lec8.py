'''
lec8
'''

#function

def my_function(a,b):
    result=a+b
    return result
    
print(my_function(1,2))

#arguments and parameters

def my_function(a,b=0):
    print(a)
    print(b)
    result = a+b
    return result
print(my_function(2,1))


#ex 1 cal abs values

def cal_abs(a):
    if a>=0:
        return a
    if a<0:
        return -a
print(cal_abs(0))
   
#ex 2

def cal_s(n,m):
    result = 0

    for i in range (n,m+1):
    
        result = result + i
        
    return result
print(cal_s(1,6))


def cal_s(n,m):

    result = 1
    
    for i in range(n,m+1): 

        result = result * i
        
    return result
    
print(cal_s(1,6))

#ex3 recursive

def cal_f(m):
    if m ==0:
        return 1
    else:
        return m*cal_f(m-1)
    
print (cal_f(0))

