tuple is similar to list but they are immutable
cant be appended,changed .if we want to change we have to redefined it.

x=(0,0,2,2)
x[0]=5 #not working xxx
x.append(3) # not working xxx

x=[[],(),[[],[],[3,4,5]]] #list ,tuple inside of list