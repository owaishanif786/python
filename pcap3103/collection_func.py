from functools import reduce

domain = [1,2,3,4,5]

our_range = map(lambda num:num*2, domain)
print(list(our_range));

evens = filter(lambda num:num%2==0, domain)
print(list(evens))

the_sum = reduce(lambda acc,num: acc+num, domain, 0) #type will infered based on first value we provide
print(the_sum)

#sorting by default
words = ['Boss', 'a', 'Alfred', 'fig', 'Daemon', 'dig']
print('Sorting by default')
print(sorted(words))

#sorting with lambda key
print("[I] Sorting with lambda key")
print(sorted(words, key=lambda word: word.lower()))


#sorting using list method
#list .sort method changes the original list while `sorted` method returns the new list
#in sorted use key to change the input for softed
print("[I] sorting using list method")
words.sort(key=str.lower, reverse=True)
print(words)

#str.upper("string") and "string".upper() are equal
assert str.upper(words[0]) == words[0].upper()
