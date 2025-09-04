print("hur gammal är du")

age = input()
age = int(age)

if age < 18: 
    print("du är ett barn")

elif age == 18:
    print("du är 18")


elif age >= 18 and age <50:
    print("du är vuxen")

elif age >= 50:
    print("du är expired")

elif age:
    print("jag vet inte")

elif age != 72:
    print("aaaaaaaaaaaa")

