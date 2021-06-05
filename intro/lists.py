my_list = [1,2,3,4,5]

#get value on some index
my_list[1] #2


#slicing [start:end] but not the end value
my_list[0:2] #[1,2]

#if you skip starting value then it will be zero
my_list[:2] #[1,2]

#slicing [start:end:step]
my_list[::2] #every other item i.e [1,3,5]

#slicing reverse list or start from end
my_list[::-1] #[5,4,3,2,1]

my_list = [1,2,3,4,5]

#set some value on index
my_list[0] = 'a' #['a',1,2,3,4,5]

#seting multiple value with slice format
my_list[0:2] = [1,2] #replace first two value in list  

#removing elements using slicing
my_list[0:3] = [] #removes first 3 elements. [4,5]

#IndexError: list index out of range exception
my_list[9]
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#IndexError: list index out of range

#valueError: list.remove(x): x not in list
my_list.remove(5)
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#ValueError: list.remove(x): x not in list

#removing certain element from list
my_list.remove(4)

#remove last element pop
my_list.pop()

#IndexError: pop from empty list
my_list.pop()
#Traceback (most recent call last):
#    File "<stdin", line 1, in <module>
#IndexError: pop from empty list

#removing first element
my_list.pop(0)

#add element to the end
my_list.append(5)

#my_list.insert(index,item) add element at specific index 
my_list.insert(1,9)
#Note: if index is greater than length then it will insert at last



