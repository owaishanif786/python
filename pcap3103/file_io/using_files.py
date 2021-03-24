FILENAME = 'names.txt'

my_file = open(FILENAME, 'w+')

my_file.write('name1\n') #For single line
my_file.write('name2\n')
my_file.writelines(['name3\n', 'name4\n', 'name5\n']) #can specify multiple lines. but you still have to provide \n

my_file.close()

#Reading from file
my_file2 = open(FILENAME, 'r')
print(my_file2.read())
print(my_file2.read()) #this will be empty as cursor is at the end of file
my_file2.seek(0) #we moving cursor to start of the file again
print(my_file2.read()) #reading file again all

my_file2.seek(0)

for line in my_file2.readlines():
    print(line)

my_file2.close()


#as "with" statement block will end it automatically close the file also
with open(FILENAME, 'w+') as my_file3:
    print("[I] writing 'with' statement")
    my_file3.write('line1\n')
    my_file3.write('line2\n')
    my_file3.writelines(['line3\n', 'line4\n', 'line5\n'])


myfile4 = open(FILENAME, 'r')
with myfile4:
    print("[I] Reading 'with' statement")
    print(myfile4.read())




