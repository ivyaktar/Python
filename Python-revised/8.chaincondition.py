x=7
y=8
z=0

result1 =x==y
result2=y>x
result3=z<x+2

result4=result1 or not result2 or result3 # 'not' just flips it
print(result4)

print(not(False and True)) # sudhu true and true e result true otherwise sobh false
print(not(False or True)) ## sudhu false and false e result false otherwise sobh true

print(not (False and True or True)) #flase

## order comes like that
"""
not 
and
not """