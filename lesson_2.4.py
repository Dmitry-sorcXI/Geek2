prices_mag = [25 , 43 , 34.50 , 58.30 , 70 , 50.50 , 11.11 , 75 , 12.11 , 39,12 , 15 , 16]

print = (f"\n\n{'*' * 35} A_1\n")

for i in prices_mag:
    rub, kop = str(f"{i:.2f}").split(".")
    print(f"{rub} руб {int(kop):02d} коп," , end=" ")