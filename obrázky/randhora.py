from tkinter import *

from tkinter import messagebox
import random
seed = random.randint(0,10000000)
print(seed)
random.seed(seed)

top = Tk()
SIZE = 500
C = Canvas(top, bg = "#000000", height = SIZE, width = SIZE)

Hx = 0
Hy = 0


def hexovac(cislo):
    hexcislo =  hex(cislo)[2:]

    if len(hexcislo) == 1:
        return "0" + hexcislo
    else:
        return hexcislo

def hexCodeFromRgb(red, green, blue):
    hexRed = hexovac(red)
    hexGreen = hexovac(green)
    hexBlue = hexovac(blue)

    return f'#{hexRed}{hexGreen}{hexBlue}'

#opakovani, smer
def ctvercovac (Horx, Hory, vel, barva):
    C.create_rectangle(Horx, Hory, Horx + SIZE, Hory + SIZE, fill=barva)

while SIZE > 10:
    opakovani = random.randint(1, 5)

    smer = random.choice([(1, 1), (1, -1), (-1, -1), (-1, 1)])
    print(smer, "smer")

    for vel in range(0, opakovani):

        Hx -= 5*smer[0] - 5 # odstraněním 5 vyjdu z  obrazu pomaleji
        Hy -= 5*smer[1] - 5 # + 5 strana chodby
        SIZE -= 5
        if SIZE > 10:
            barva = hexCodeFromRgb(random.randint(0, 240), random.randint(0, 240), random.randint(0, 240))

            C.create_rectangle(Hx, Hy, Hx + SIZE, Hy + SIZE, fill=barva)


C.pack()
mainloop()