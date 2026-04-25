x=[x+5 for x in range(5)] 
x=[x%5 for x in range(5)] 
x=[0 for  x in range(5)] 
x=[[0 for x in range(100)] for x in range(5)] 
x=[i for i in range(100) if i%5 ==0 ] 
x={i:0 for i in range(100) if i%5 ==0 }
x={i for i in range(100) if i%5 ==0 }
x=(i for i in range(100) if i%5 ==0 )
x=tuple (i for i in range(100) if i%5 ==0 )

print(x)