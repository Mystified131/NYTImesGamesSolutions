
import enchant
from itertools import  permutations

d = enchant.Dict("en_US")

oplst = []

for x in range(7):
    print("")
    letr = input("Please enter one letter, then press enter: ")
    oplst.append(letr.lower())

print(""
)
keyletr = input("What is the key letter, please?: ")

print("")

print("Thank you.")

print("")

print("This may take a moment.")


wdlst = []

worm = list(permutations(oplst, 4))
worn = list(permutations(oplst, 5))
woro = list(permutations(oplst, 6))
worp = list(permutations(oplst, 7))
worq = list(permutations(oplst, 8))
worf = list(permutations(oplst, 9))
wort = list(permutations(oplst, 10))
worl = list(permutations(oplst, 10))
wory = list(permutations(oplst, 10))

wor = ""

for elem in worm:

    astr = ""

    for wor in elem:
        astr += wor

    if d.check(astr) and astr not in wdlst and keyletr in astr:

        wdlst.append(astr)


for elem in worn:

    astr = ""

    for wor in elem:
        astr += wor

    if d.check(astr) and astr not in wdlst and keyletr in astr:

        wdlst.append(astr)

for elem in worq:

    astr = ""
    
    for wor in elem:
        astr += wor

    if d.check(astr) and astr not in wdlst and keyletr in astr:

        wdlst.append(astr)

for elem in worf:

    astr = ""
    
    for wor in elem:
        astr += wor

    if d.check(astr) and astr not in wdlst and keyletr in astr:

        wdlst.append(astr)

for elem in wort:

    astr = ""
    
    for wor in elem:
        astr += wor

    if d.check(astr) and astr not in wdlst and keyletr in astr:

        wdlst.append(astr)

for elem in worl:

    astr = ""
    
    for wor in elem:
        astr += wor

    if d.check(astr) and astr not in wdlst and keyletr in astr:

        wdlst.append(astr)

for elem in wory:

    astr = ""
    
    for wor in elem:
        astr += wor

    if d.check(astr) and astr not in wdlst and keyletr in astr:

        wdlst.append(astr)

print("")

print(wdlst)

outfile = open("BeeSolution.txt", "w")

for elem in wdlst:
    outfile.write(elem + '\n')

outfile.close()