import sys

file_name = 'recepies.txt'

try:
    my_file = open(file_name, 'x')
    # my_file.write('Meatballs\n')
    my_file.write(b'Meatballs\n')
    my_file.close()
except FileExistsError as err: 
    print(f"The  {file_name} already exists")
except: #general exception block
    print(f"Unable to write to file")
else: #this will if there is no error in try block
    print(f"wrote to {file_name}")
finally: #this will always run
    print(f"Execution completed")
