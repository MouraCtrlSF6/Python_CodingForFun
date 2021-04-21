print("------------ Pentagon Numbers ------------")
def pen_num(var):
    var=1+2.5*var*(var-1)
    return var

var=int(input("Type a number: "))
var=int(pen_num(var))
print(f"\nThe area, in dots, of this element is: {var}\n\n")