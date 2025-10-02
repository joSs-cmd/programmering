sentence = input("Skriv en mening som innehåller åäö: ")

new_sentence = ""

for letter in sentence:
    if letter in "ö" "Ö":
        new_sentence += "o"
    elif letter in "å" "Å":
        new_sentence += "a"
    elif letter in "ä" "Ä":
        new_sentence += "a"
    else:
        new_sentence += letter

print(new_sentence)