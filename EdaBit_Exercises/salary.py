def calc(ph, hr):
    brute = 22*ph*hr
    INSS = brute*0.08
    IR = brute*0.11
    Sind = brute*0.05
    liquid = brute - (INSS + IR + Sind)
    data = [brute, INSS, IR, Sind, liquid]
    return data
    
ph = float(input("How much do you earn per hour: "))
hr = float(input("Hou many hours you work per day: "))
data = calc(ph, hr)
data_str = ["brute", "INSS", "IR", "Sind", "liquid"]
print("\n")
for i in range(5):
    print(data_str[i],": R$", data[i])