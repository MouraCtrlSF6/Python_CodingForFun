def mimics(a, b):
    return int(a/(2**b))

a = int(input("Type the begging value: "))
b = int(input("Type the right shifting value: "))
r = mimics(a, b)
print("Resulting number: ", r)