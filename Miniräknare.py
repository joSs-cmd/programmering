print("Välkommen till miniräknaren!")

tal1 = float(input("Ange första talet: "))
tal2 = float(input("Ange andra talet: "))

print("Vad vill du göra med dessa tal?")

print("1. Addera")
print("2. Subtrahera")
print("3. Multiplicera")
print("4. Dividera")

val = input("Välj operation (1-4): ")

if val == "1":
    print("Resultat:", tal1 + tal2)
elif val == "2":
    print("Resultat:", tal1 - tal2)
elif val == "3":
    print("Resultat:", tal1 * tal2)
elif val == "4":
    if tal2 == 0:
        print("Fel: kan inte dividera med 0!")
    else:
        print("Resultat:", tal1 / tal2)
else:
    print("Ogiltigt val, försök igen!")
