# Some Useful modules

## Random moudles

random.random returns float betweens 0.0 to 1

seed is used to create some preditcable randomness for testing.
random.seed(10) #0.5714025946899135
random.seed(10) #0.5714025946899135
we ran random two times and with seed and at both times it was having same value. so this can be very useful in testing


choice will give single result from a dataset
x = "WELCOME"
random.choice(x) #E

sample will give us new dataset from parent dataset.
list1 = [1,2,3,4,5]
sample(list1, 3) # [2,3,5]

shuffle is used to shuffle some predefined dataset
def myfunction():
    return 0.1
mylist = ['a','b','c']
random.shuffle(mylist, myfunction)


## platform modules

have machine information
dir(platform)
platform.machine() #x86_64
platform.system() #Linux
platform.node() #machineName
platform.platform() #Linux-5.8.0-45-generic-x86_64-with-debian-bullseye-sid
