import pdb

def map(func, values):
    output_values = []
    index = 0
    while index < len(values):
        pdb.set_trace()
        output_values.append(func(values[index]))
        index+=1
    return output_values

def add_one(val):
    return val+1

print(map(add_one, list(range(10))))


#(Pdb) values
#(Pdb) index
#h for help in pdb
#list
#next
#continue

#Run debugger from CLI
# python3.7 -m pdb debugging.py 
#break 5, index == 5
#
