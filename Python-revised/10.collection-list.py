##List and touple

x=[4,True,'hi'] #any type
x.append('hello')
x.extend([44,5,77,'lo'])

y='hi'
print(len(x),len(y)) #works fine
print(x.pop())
print(x.pop(0))
print(x.pop())
x[0]='hello'
print(x)
print(x[0])

x=[4,True,'hi']
y=x # x and y both storing refrence of list , not copy
x[0]='hello'
print(x,y) # exact same

y=x[:] #copy of this list change korle its not applied to other list 
 




