
#tuples are useful where order matters. notice brackets type
point = (2.0, 3.0)

#can access using index
point[0]

#they are immutable/unchangeable
point[0] = 1
#Traceback (most recent call last):
#    File "<stdin>", line 1, in <module>
#TypeError: 'tuple' object does not support item assignment


point_3d = point + (4.0,)

#they can be useful from function return call
x,y,z = point_3d
#now x=2.0, y=3.0 and z=4.0

#number of values in tuple on right must match total number of variables on right
x,y = point_3d
#Traceback (most recent call last):
#    File "<stdin>", line 1, in <module>
#ValueError: too many values to unpack (expected 2)

#tuple substitution in string
print('My name is: %s %s' % ("owais", "h"))

#For tuple substituion arguments must match
'My name is: %s %s %s' %("owais", "h")
#Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#TypeError: not enough arguments for format string

'My name is %s %s ' %('m', "owais", 'h')
#Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
#TypeError: not all arguments converted during string formatting



#Ranges
range(10)
range(0,10000)
list(range(10))
range(1,12,2)
