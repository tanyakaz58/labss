import math
a=math.pi/5
b=math.pi
h=math.pi/25
y=0
s=0
x=a
if a<=x<=b:
    while x>0.0001:
        for i in range (1,100):
            y=(x**2-(math.pi**2)/3)/4
            s=s+(((-1)**i)*(math.cos(i*x))/(i**2))
            print (y, 'Значение y')
            x=x-h
else:
    print ("ОШИБКА")
print (s, 'Значение S')
