
import enchant
from itertools import  permutations

d = enchant.Dict("en_US")

wordstt = ["LORE", "HERO", "CANT", "SURE", "SELL", "KINE", "PEON", "LICE", "ALTI", "RISE", "LINK", "LIRA", "IMAM", "FONE", "CALM", "FENCE", "CONIC", "NURSE", "VALES", "RETAG", "STAMP", "ALTER", "DEBATE", "THETICAL"]

letlst = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

dblst = []
for elem in letlst:
    dblst.append(elem)
    dblst.append(elem)

woof = list(permutations(dblst, 2))

wiff = []

wiff = list(set(woof))

worg = []

for elem in wiff:
    subl = []
    for ltr in elem:
        subl.append(ltr)
        subl.append(ltr)
    worg.append(subl)

solvlst = []

for wd in wordstt:
    z = len(wd) + 4
    minilst = []
    sublst = []
    for el in wd:
        sublst.append(el)
    
    for rog in worg:
        sub2lst = []
        for weg in rog:
            sub2lst.append(weg)
        for tab in sublst:
            sub2lst.append(tab)
        wigg = list(permutations(sub2lst, z))

        for trib in wigg:
                   
            wordstr = ""
            for lotr in trib:
                wordstr += lotr

            if d.check(wordstr) and wordstr not in minilst:

                print(wordstr)
                minilst.append(wordstr)

    solvlst.append(minilst)

print(solvlst)









