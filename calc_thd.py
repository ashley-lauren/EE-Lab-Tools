from math import sqrt

print("Calculate the THD for FFT analysis of a voltage function")
print("Enter a non-digital string at any point to end input and return THD")
vals = []
cont = True
top = 0
temp = input("Fundamental dbV value: ")

while (cont == True and len(temp) > 0):
    try:
        rms = 10 ** (float(temp) / 20)
        vals.append(float(rms))
        temp = input("Harmonic {n} dbV value:".format(n=len(vals)))
    except ValueError:
        cont = False

if (len(vals) > 0):
    for i in range(1, len(vals)):
        top += vals[i] ** 2

    print("THD %: " + str(100 * round((sqrt(top) / vals[0]), 4)))
else:
    print("Empty list")
