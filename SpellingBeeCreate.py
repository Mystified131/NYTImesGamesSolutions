
import enchant
from itertools import  permutations
import datetime
import random

right_now = datetime.datetime.now().isoformat()
tlist = []

for i in right_now:
    if i.isnumeric():
        tlist.append(i)

tim = ("".join(tlist))

d = enchant.Dict("en_US")

conlst = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z"]
vowlst = ["A",  "E",  "I", "O", "U", "Y"]

sublst = []

for x in range(26):
    ctr = random.randrange(10)
    if ctr < 5:
        vch = random.randrange(6)
        letch = vowlst[vch]
    if ctr > 4:
        cch = random.randrange(20)
        letch = conlst[cch]
    if letch not in sublst:
        sublst.append(letch)

oplst = []

for x1 in range(7):
    astr = sublst[x1]
    oplst.append(astr)

x2 = random.randrange(7)
keyletr = oplst[x2]


biglst = []

for elem in oplst:
    for x in range(2):
        biglst.append(elem)        

print("")                   

print(oplst)

print(keyletr)

print("")

print("This may take a moment.")

print("")

print("Here are the solutions, if there are any:")

print("")

print("Check for modern parlance. Some may not appear in NY Times word list:")

print("")

wdlst = []

worm = list(permutations(biglst, 4))

for elem in worm:

    astr = ""

    for wor in elem:
        astr += wor

    if d.check(astr) and astr not in wdlst and keyletr in astr:

        print(astr)

        wdlst.append(astr)

worm = []

worn = list(permutations(biglst, 5))

for elem in worn:

    astr = ""

    for wor in elem:
        astr += wor

    if d.check(astr) and astr not in wdlst and keyletr in astr:

        print(astr)

        wdlst.append(astr)
        
worn = []

woro = list(permutations(biglst, 6))

for elem in woro:

    astr = ""

    for wor in elem:
        astr += wor

    if d.check(astr) and astr not in wdlst and keyletr in astr:

        print(astr)

        wdlst.append(astr)
        
woro = []

#worp = list(permutations(biglst, 7))

#for elem in worp:

    #astr = ""

    #for wor in elem:
        #astr += wor

    #if d.check(astr) and astr not in wdlst and keyletr in astr:

        #print(astr)

        #wdlst.append(astr)

#worp = []
                
print("")

print(wdlst)

print("")

titstr = "SpellingBeeCreation." + tim + ".txt"

outfile = open(titstr, "w")

outfile.write ("A Tenable Spelling Bee Creation." + '\n' )
outfile.write ("" + '\n' )
outfile.write ("Time: " + tim + '\n')
outfile.write ("" + '\n' )

for elem in oplst:
    outfile.write(elem + ",")
outfile.write('\n')
outfile.write (keyletr + '\n' )
outfile.write ("" + '\n' )

outfile.write('\n')
outfile.write ("" + '\n' )

for elem in wdlst:
    outfile.write(elem + '\n')

outfile.close()

print("")

print("See the output document in the same folder as your code.")

print("")

## THE GHOST OF THE SHADOW ##