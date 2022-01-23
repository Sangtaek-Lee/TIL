# ax**2 + bx + c = 0 (a != 0)  
from cmath import sqrt
from logging import root

a = float(input('Enter a: '))  
b = float(input('Enter b: '))  
c = float(input('Enter c: '))    
d = (b**2) - (4*a*c)  

sol1 = (-b-sqrt(d))/(2*a)  
sol2 = (-b+sqrt(d))/(2*a)  
print('근1 : {0}, 근2 : {1}'.format(sol1,sol2))