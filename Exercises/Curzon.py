def is_curzon(x):
    y = 2**x + 1
    z = 2*x + 1

    return y % z == 0

print("Curzon numbers")
x = int(input("Type a number: "))
aux = is_curzon(x)

if aux:
    print(f"{x} is a curzon number.")
else:
    print(f"{x} is not a curzon number")
