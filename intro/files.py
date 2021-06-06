my_file = open('xmen.txt', 'w+')
my_file.write('Beast\n')
my_file.writelines(["east\n", 'west\n', 'south\n'])

my_file.close()


my_file = open('xmen.txt', 'r')
print(my_file.read()) 
print('reading again') 
print(my_file.read()) #empty because cursor is at end
my_file.seek(0) #move curstor to start
my_file.close()


#with open will automatically close the file
with open('ymen.txt', 'w+') as my_file:
    my_file.write('Beast\n')
    my_file.write('East\n')


#second way `with` statement you can store in variable and use later
my_file = open('zmen.txt', 'w+')
with my_file:
    print(my_file.read())

