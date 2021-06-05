#in
1 in [1,2,3]

#not in
9 not in [1,2,3]

#or will return last if both are false values
0 or False
#False

#or will reuturn first value if both are true
"hello" or True
#'hello'

#and will return first  if both are false
0 and False
#0

#and will return last value if both are true
'hello' and True
#True

#iterating over tuple
point = (2.1, 3.0, 7)
for value in point:
    print(value)

#iterating over object/ditct sequeence
ages =  {'owais': 30, 'waqas': 20}
for key in ages:
    print(f"{key} is {ages[key]}")

#iterating over string sequence
for letter in "string":
    print(letter)

#iterating over list of tuples using variable packing
list_of_points = [(1,2), (2,3), (3,4)]
for x,y in list_of_points:
        print(f"x: {x} and y:{y}")

#iterating over dicts via variable packing
for name, age in ages.items():
    print(f"name: {name} and age:{age}")