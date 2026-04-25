def func():
    print('run')
    def func():
        print('hi')
    func()


func() #object call


def func(x,y):
    print('run',x,y)
    return x*y, x/5 #return in tuple 
    


print (func(5,6)) 
r1, r2 = func(5,6)
print(r1,r2)  



def func(x,y, z=None):
    print('run',x,y,z)
    return x*y, x/y #return in tuple 
    


print (func(5,6)) 
r1, r2 = func(5,6,7)
print(r1,r2)  