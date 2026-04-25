''' Sets
is simply an unordered unique collection of elements. What that means is there is no duplicate elements. We
do not keep track of order or frequency of elements. All we care about is if something is there, or if
something is not there, the reason we do this is because the set is extremely fast to do. What's called look-ups
removals or additions'''

[2,2,12,2,12,12]

x=set() #empty set
s={} dict
s={4,32,2,2}

print(s)
s.add(5)
s.remove(2)
print(4 in s) #true
s2={3,4,22,1}
print(s.intersection(s2))
