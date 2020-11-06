import sys

if len(sys.argv) == 2:
    _ , input_file = sys.argv
else:
    print("vlož pouze název souboru který chceš zkontrolovat")
    exit()

spravnost_zavorek = True
poloha = 0
typ_zavorky = ""
chyba_zavorky = 0

pocet_jednoduchych = 0 # ()
pocet_lomenych = 0 # <>
pocet_ctvercovych = 0 # []
pocet_slozenych = 0 # {}

zavorky = [pocet_jednoduchych, pocet_lomenych, pocet_ctvercovych, pocet_slozenych]
nazvy_zavorek = [")",">","]","}"]
zavorecky = "()<>[]{}"
print(zavorky)

def aktualizuj():
    global zavorky
    zavorky = [pocet_jednoduchych, pocet_lomenych, pocet_ctvercovych, pocet_slozenych]

with open(input_file) as file:
    f = file.read()
    print(type(f))


for pismeno in f: # šlo by to zkrátit listem v t

    if pismeno == "(":
        pocet_jednoduchych += 1
    elif pismeno == ")":
        pocet_jednoduchych -= 1

    elif pismeno == "<":
        pocet_lomenych += 1
    elif pismeno == ">":
        pocet_lomenych -= 1

    elif pismeno == "[":
        pocet_ctvercovych += 1
    elif pismeno == "]":
        pocet_ctvercovych -= 1

    elif pismeno == "{":
        pocet_slozenych += 1
    elif pismeno == "}":
        pocet_slozenych -= 1


    p=0
    aktualizuj() #šlo by to taky udělat prostym výčtem tohle mi ale přijde takový elegantnější
    for zavorka in zavorky:
        if zavorka < 0 :

            typ_zavorky = nazvy_zavorek[p]
            chyba_zavorky = 1
            break  #obě loops by šlo taky přerušit za pomocí else:  (for in:, for in: break, else: continut, break)
        p += 1
    else:
        poloha += 1
        continue

    break





if chyba_zavorky != 1:
    p = 0

    for zavorka in zavorky:

        if zavorka > 0 :

            typ_zavorky = nazvy_zavorek[p]
            chyba_zavorky = 2
        p += 1


if chyba_zavorky == 0:
    print("zavorky jsou v textu správně")
elif chyba_zavorky == 1:
    print(f"přebývající závorka {typ_zavorky} na místě {poloha + 1}. znaku")
else:
    print(f"chybí {typ_zavorky}")