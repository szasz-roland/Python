doIng = str(input("'F' faranheitet akarsz celsiusba 'C' ha fordítva >"))

if doIng == "F":
    faranheit = float(input("Add meg a faranheit értékét> "))
    print((faranheit - 32) / 1.8)
elif doIng == "C":
    celsius = float(input("Add meg a celsius fokot> "))
    print((celsius * 1.8) + 32)
