def contact_card(name, age, car_model):
    return f"{name} is {age} and drives a {car_model}"

#calling args in sequence
contact_card("owais", 28, "bonusCar")

#if calling out of order then you have to specify name and value
contact_card(age=28, car_model="f1", name="owais")

#Positional argument follows keyword argument

contact_card(age=28, "keith", car_model="civic")
#File "<stdin>", line 1
#SyntaxError: positional argument follows keyword argument


#default arguments
def can_drive(age, drive_age=16):
    return age >= drive_age

can_drive(15) #False
