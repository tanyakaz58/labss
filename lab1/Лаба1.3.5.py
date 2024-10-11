import math
a=math.pi/5
b=math.pi
h=math.pi/25
x=a
y=0
m=0
s=0
while m<0.0001 and a<=x<=b:
    y=(x**2-(math.pi**2)/3)/4
    print (y, 'Значение y')
    x=x-h
    for i in range (1,300):
        m=(((-1)**i)*(math.cos(i*x))/(i**2))
        s=s+m
    print (s, 'Значение s')

        
    
