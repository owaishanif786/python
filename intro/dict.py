#a map like thing with key value pairs
ages = { 'owais': 30, 'sikandar': 42}

#accessing pair value via specifing key
ages['owais']

#keys are immutable

#removing some key

del ages['owais']

#removing variable
del ages

#popping some key
ages.pop('owais')

ages.keys()
#dict_keys(['owais'])

ages.values()

#converting keys/values to list
list(ages.values())

#using dict keyword. don't use quotes for string when using dicts
weights = dict(owais=80, waqas=100)
#{'owais': 80, 'waqas': 100}

#creating dict using tuples, pass a list of tuples to dict
colors = dict([('owais', 'red'), ('waqas', 'blue')])
