from tkinter import *
import time
from tkinter import messagebox
import random
seed = random.randint(0,10000000)
print(seed)
random.seed(seed)

top = Tk()
size = 500
C = Canvas(top, bg = "#000000", height = size, width = size)
SIZE = size

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
chodba = random.choice([True, False])

while SIZE > 10:
    opakovani = 1 #random.randint(1, 5)

    smer = random.choice([(1, 1), (1, 0), (0, 0), (0, 1)])

    print(chodba)
    for vel in range(0, opakovani):

        Hx += random.randint(2,5)  # trochu zajímavější je možná 5*smer[0]
        Hy += random.randint(2,5)# a 5*smer[1]
        SIZE -= 7

        if SIZE > 2 and chodba == True:
            barva = hexCodeFromRgb(random.randint(0, int(SIZE/3)), random.randint(0, int(SIZE/3)), random.randint(0, int(SIZE/3)))
            C.create_rectangle(Hx, Hy, Hx + SIZE, Hy + SIZE, fill=barva)
        elif SIZE > 2 :
            barva = hexCodeFromRgb(random.randint(100 - int(SIZE/5), 200), random.randint(100 - int(SIZE/5), 200), random.randint(100 - int(SIZE/5), 200))
            C.create_rectangle(Hx, Hy, Hx + SIZE, Hy + SIZE, fill=barva)
        else:
            break


C.pack()


mainloop()


