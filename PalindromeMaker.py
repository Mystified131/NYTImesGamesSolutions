
import enchant
import random

d = enchant.Dict("en_US")

wordstt = ["LORE", "HERO", "CANT", "SURE", "SELL", "KINE", "PEON", "LICE", "ALTI", "RISE", "LINK", "LIRA", "IMAM", "FONE", "CALM", "FENCE", "CONIC", "NURSE", "VALES", "RETAG", "STAMP", "ALTER", "DEBATE", "THETICAL"]

conlst = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z"]
vowlst = ["A",  "E",  "I", "O", "U", "Y"]

sollst = []

for fish in range(40000):

    wlen = random.randrange(3, 8)

    wdlt = []

    for x in range(wlen):
        ctr = random.randrange(10)
        if ctr < 5:
            vch = random.randrange(6)
            letch = vowlst[vch]
        if ctr > 4:
            cch = random.randrange(20)
            letch = conlst[cch]
        wdlt.append(letch)

    wordsam = ""

    lettot = len(wdlt)

    for x in range(lettot):
        wordsam += wdlt[x]
    for x2 in range((lettot - 1), -1, -1):
        wordsam += wdlt[x2]

    print(wordsam)

    if d.check(wordsam):
        sollst.append(wordsam)
        print("Correct: ", wordsam)

print(sollst)


