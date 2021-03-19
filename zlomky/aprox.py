"""cíl: dostanu desetinné číslo, a já mám vyhodit nejpřesnější aproximace,
        respektive: desetiné číslo převést co nejpřesněji na zlomek

    postup:
    -  ve for lupu projedeu možné dělitele od 2 do 999
    - vynásobím číslo dělitelem, toto číslo zaokrouhlým a následně znovu vydělím, odečtu od prvního čísla, tuto "odlišnost" od základního čísla použiju jako skore které vrátím funkcí
    - získané skore prorovnám s zatím-nejlepším, v případě že je menší uložím score spolu s dělitelem na post nejlepšího
    -   při navýšení cifry dělitele a při posletním děliteli, se dělitel uloží do seznamu nejlepších kombinací
    - poté co budou prozkoumány všichni dělitelé se prověří jestli nejsou v seznamu dva stejní dělitelé a přebyteční se vymažou
    - nakonec se se výslední dělité vy#ujou
    -
    """
import math
TheNum = float(input("give it to me: "))



score = math.inf
maybeTheOne = 1111
vysledky = [1111,1111,1111]

"""def chekovac(ex,delit):
    sc = TheNum - ex/delit"""


for delit in range(1, 1000):
    expnum = abs(round(TheNum * delit))
    ##(TheNum * delit, "naso")
    ##(expnum, "zao")
    for x in [-1,0,1]:

        sc = abs(TheNum) - (expnum+x)/delit

        ##(sc,"sc",score)
        #(sc, expnum, x, delit)
        if  abs(sc) < score:
            #("ini")
            score = abs(sc) #případně zařídit aby se kód nemusel opakovat
            if x == -1:
                x=2
            maybeTheOne = int(str(delit) + str(x))
            #(maybeTheOne,"maybe")

    if delit == 99 or delit == 9 or delit == 999:
        #(str(delit), len(str(delit)), #(delit))
        vysledky[len(str(delit))-1] = maybeTheOne

#(vysledky)


if vysledky[0] == vysledky[2]:
    del vysledky [1:3]
elif vysledky[0] == vysledky[1] or vysledky[1] == vysledky[2]:
    del vysledky[1]
if 1111 in vysledky:
    vysledky.remove(1111)

#("here am i")
for jmenovatel in vysledky:
    #(jmenovatel)
    if TheNum < 0: TheNum* -1
    y = int(str(jmenovatel)[-1])
    jmenovatel = int(str(jmenovatel)[:-1])
    #(jmenovatel)
    if y ==2:
        y=-1
    čitatel = round(jmenovatel* TheNum) + y
    #(jmenovatel)
    print(čitatel,"/", str(jmenovatel))

