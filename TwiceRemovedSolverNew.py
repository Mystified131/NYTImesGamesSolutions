
import enchant
from itertools import  permutations

d = enchant.Dict("en_US")

wordstt = ["LORE", "HERO", "CANT", "SURE", "SELL", "KINE", "PEON", "LICE", "ALTI", "RISE", "LINK", "LIRA", "IMAM", "FONE", "CALM", "FENCE", "CONIC", "NURSE", "VALES", "RETAG", "STAMP", "ALTER", "DEBATE", "THETICAL"]

conlst = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z"]
vowlst = ["A",  "E",  "I", "O", "U", "Y"]

wiff = []

for elem in conlst:

    for elem2 in vowlst:

        wiff.append([elem, elem2])
        wiff.append([elem2, elem])

solvlst = []

for wd in wordstt:
    elemlst = []
    z = len(wd) + 4
    y = len(wd) + 2
    minilst = []
    

    for bam in wiff:
        sublst = []

        for el in wd:
            sublst.append(el)

        sublst.append(bam)
        sublst.append(bam)

        elemlst.append(sublst)

        wigg = list(permutations(sublst, y))

        for trob in wigg:

            teststr = ""

            for lat in trob:
                if len(lat) == 1:
                    teststr += lat
                if len(lat) == 2:
                    teststr += lat[0]
                    teststr += lat[1]

            if d.check(teststr) and teststr not in minilst:

                print(teststr)

                minilst.append(teststr)
                   

    solvlst.append(minilst)

print(solvlst)









