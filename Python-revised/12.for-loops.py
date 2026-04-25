while loop is infinite

for i in range (-10,-1,-1): #start,stop,step
    print(i)




ekta argument thakle or one number pass hoile by default =stop bojhai (0 theke stop-1)
2 ta argument thakle start,stop
3 ta argument thakle start,stop,step

#list eo
for i in [3,4,42,3,2,4]:
    print(i)

x=[3,4,42,3,2,4]
for i in range(len(x)):
    print(x[i])


for i, element in enumerate(x): #create indexes and values for all elements
    print(i,element)
