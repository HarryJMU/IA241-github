'''
lec3
'''

my_list = [1,2,3,4,5]

print(my_list)

my_nested_list = [1,2,3,[1,2,3,4,5]]

print(my_nested_list)

my_list[0]=6 
print(my_list)

print(my_list[0])
print(my_list[1])
print(my_list[-1])

print(my_list)
print(my_list[1:3])
print(my_list[:])

x,y = ['a','b']
print(x)
print(y)

print(my_list)
my_list.append(7)
print(my_list)

my_list.remove(7)
print(my_list)

my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)

print(my_list + [8,9])

my_list.extend(['a','b'])
print(my_list)

print('a' in my_list)

print( len(my_list))

print('hello\tworld')

print('hello\nworld')

print(  len('hello world'))

print( 'hello world'[2])

my_letter_list = ['a','a','b','b','c']
print(my_letter_list)

print (set(my_letter_list))

my_unique_letter=set(my_letter_list)

print(my_unique_letter)

print (len(my_unique_letter))

print ('d' in my_unique_letter)

print(list(my_unique_letter)[0])
