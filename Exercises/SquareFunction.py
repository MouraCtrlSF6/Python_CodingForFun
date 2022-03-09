import math
def polynomial (a, b, c):
    delta = (b**2) - 4*a*c
    if delta<0:
        delta = math.sqrt(delta*(-1))
        p1 = round(-b/(2*a), 2)
        p2 = round(delta/(2*a), 2)
        s_x1 = str(p1) + ' + ' + str(p2) + 'i'
        s_x2 = str(p1) + ' - ' + str(p2) + 'i' 
        return s_x1, s_x2
    else:
        delta = math.sqrt(delta)
        x1 = round((-b + delta)/(2*a), 2)
        x2 = round((-b - delta)/(2*a), 2)
        return x1, x2

a = int(input("Type the a parameter: "))
b = int(input("Type the b parameter: "))
c = int(input("Type the c parameter: "))
x1, x2 = polynomial(a, b, c)

print(f"\nFunction's law is: {a}x^2 + {b}x + {c}")
print(f"The function roots are {x1} and {x2} .\n")