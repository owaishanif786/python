from vehicle import Vehicle 

v = Vehicle('4-cyclider', ['front-driver', 'front-pasenger', 'rear-driver', 'rear-pasenger'])
#print(v.engine)
v.description()

#we can treat vehcile object as namespace and can add attributes at runtime

#adding attributes at runtime
v.serial_number = '1234'
print(f'Serial Number: {v.serial_number}')

#removing attirbute at runtime
del v.serial_number

#this will throw error because we have now delete the serial number attribute from Vechicl instance
print(f'Serial Number: {v.serial_number}')