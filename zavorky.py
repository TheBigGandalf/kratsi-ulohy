import sys

if len(sys.argv) == 2:
    _ , input_file = sys.argv
else:
    print("vlož pouze název souboru který chceš zkontrolovat")
    exit()


poloha = 0

zavory = "(<[{)>]}"
posledni_zavorka = ""
tz= []
otevrena= []

with open(input_file) as file:
    f = file.read()
    print(type(f))

poloha = -1
for znak in f:
    poloha += 1
    if znak in zavory:
        print("A")

        if zavory.find(znak) < 4:
            otevrena.append(znak)
            print(otevrena)

        else:
            if znak == zavory[zavory.find(otevrena[-1]) + 4]:
                otevrena.pop()
            else:
                print(f"chybí {zavory[zavory.find(otevrena[-1]) + 4]} závorka, nebo přebývá zavorka {znak} na místě {poloha} ")
                exit()

print(otevrena)
prebyvajici = ""
if len(otevrena) == 0:
    print("závorky jsou správně")
elif len(otevrena) == 1:
    print(f"přebývá {otevrena[0]} závorka")
else:
    for zavorka in otevrena:
        prebyvajici += " " + zavorka
    print(f"přebývají {prebyvajici} závorky")


