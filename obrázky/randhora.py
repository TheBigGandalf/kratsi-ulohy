#zkusit


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
sirska = 8
PORADI = 0

pohyby = []
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
class ctverec :
    """vytvorim ctverec, zapamatuju si relativni postaveni vůči předcházejícímu čtverci, umistím ho do společného listu,
    funkci na posouvání ctverce o pocet z listu podle poradi
    """
    def __init__(self,o, p):
        
        
        self.pohx = 0
        self.pohy = 0
        self.poradi = por
        self.sire = 0

    def vytvor(self):
        global Hx, Hy, SIZE, sirska, pohyby
        for vel in range(0, opakovani):
            self.pohx = random.randint(2,5)
            self.pohy = random.randint(2,5)

            Hx += self.pohx # trochu zajímavější je možná 5*smer[0]
            Hy += self.pohy # a 5*smer[1]
            pohyby.append((self.pohx,self.pohy))
            SIZE -= sirska
            self.sire = SIZE

            if SIZE > 2 and chodba == True:
                barva = hexCodeFromRgb(random.randint(0, int(SIZE/3)), random.randint(0, int(SIZE/3)), random.randint(0, int(SIZE/3)))
                self.ctvr = C.create_rectangle(Hx, Hy, Hx + SIZE, Hy + SIZE, fill=barva)
            elif SIZE > 2 :
                barva = hexCodeFromRgb(random.randint(100 - int(SIZE/5), 200), random.randint(100 - int(SIZE/5), 200), random.randint(100 - int(SIZE/5), 200))
                self.ctvr = C.create_rectangle(Hx, Hy, Hx + SIZE, Hy + SIZE, fill=barva)
            else:
                break

    def jdi (self):
        global pohyby,PORADI, top
        top.move(self.ctvr,pohyby[PORADI][0],pohyby[PORADI][1])
        self.ctvr




for p in range(1,SIZE/ sirska + 1):
    opakov = 1 #random.randint(1, 5)


    #smer = random.choice([(1, 1), (1, 0), (0, 0), (0, 1)])

    ctverec(opakov, p)

#for x in range(0,10):


C.pack()


mainloop()


