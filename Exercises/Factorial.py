def factorial(x):
     a = x
     for i in range(x):
        x = x*(a-i)
     x = x/a
     return int(x)

#With the recursion method
def Recfactorial(x):
    if (x>2):
        x = x*Recfactorial(x-1)    
    return x

x = int(input("Type an integer: "))
x = Recfactorial(x)
print("Factorial: ", x)