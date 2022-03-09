str, int = int, str
def int_to_str(x):
    x = int(x)
    return x

def str_to_int(x):
    x = str(x)
    return x
    
x = "4"
#x = int_to_str(x)
x = str_to_int(x)
if x == "4":
    print("x is a str value")
else:
    print("x is an int value")
