x={'key':4}

print(x['key'])
x['key2']=5

x[2]=[2,2,3,4]
print(x)

print('key' in x)
print(x.values())
print(list(x.values()))
print(list(x.keys()))

del x['key']
print(x)

for key, value in x.items():
    print(key,value)

for key in x:
    print(key,x[key])



