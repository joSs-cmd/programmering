print("Välkommen till kiosken!")
print("Vi säljer:")
print("Glass - 20 kr")
print("Varmkorv - 15 kr")
print("Läsk - 15 kr")
print("Godis - 10 kr")

produkt = input("Vad vill du köpa? ")

if produkt == "Glass":
    pris = 20
elif produkt == "Varmkorv":
    pris = 15
elif produkt == "Läsk":
    pris = 15
elif produkt == "Godis":
    pris = 10
else:
    print("Den varan finns inte i kiosken.")
    pris = 0

if pris > 0:
    antal = input("Hur många vill du köpa? ")
    antal = int(antal)
    total = pris * antal
    print("Det blir", total, "kr.")
