x=[0,1,2,3,4,5,7,8]
y=['hi','hello','goodbye','cya','sure']
s="hello"

sliced=[0:4:2]# [start:stop:step]  #stop is excluded #just like range function 
#x[:4] stop at 4
x[2:] start at 2 and stop at end
x[2:4:] start at 2 go to 4 and step 1 or x[2:4]
sliced=s[::2] ##hlo
sliced=s[::-1] #reversed



reverse a list= x[::-1]
print(sliced)

on tuple
sliced=(1,2,3,4,4,2,2,1)[::2]