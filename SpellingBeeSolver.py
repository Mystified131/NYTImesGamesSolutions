
import enchant
from itertools import  permutations

d = enchant.Dict("en_US")

oplst = []

for x in range(7):
    print("")
    letr = input("Please enter one letter, then press enter: ")
    oplst.append(letr.lower())

biglst = []

for elem in oplst:
    for x in range(2):
        biglst.append(elem)               
                    
print(""
)
keyletr = input("What is the key letter, please?: ")

print("")

print("Thank you.")

print("")

print("This may take a moment.")

print("")

print("Here are the solutions:")

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

worp = list(permutations(biglst, 7))

for elem in worp:

    astr = ""

    for wor in elem:
        astr += wor

    if d.check(astr) and astr not in wdlst and keyletr in astr:

        print(astr)

        wdlst.append(astr)
        
worp = []

worq = list(permutations(biglst, 8))

for elem in worq:

    astr = ""

    for wor in elem:
        astr += wor

    if d.check(astr) and astr not in wdlst and keyletr in astr:

        print(astr)

        wdlst.append(astr)
        
worq = []

worf = list(permutations(biglst, 9))

for elem in worf:

    astr = ""

    for wor in elem:
        astr += wor

    if d.check(astr) and astr not in wdlst and keyletr in astr:

        print(astr)

        wdlst.append(astr)
        
worf = []

wort = list(permutations(biglst, 10))

for elem in wort:

    astr = ""

    for wor in elem:
        astr += wor

    if d.check(astr) and astr not in wdlst and keyletr in astr:

        print(astr)

        wdlst.append(astr)
        
wort = []

print("")

print(wdlst)

outfile = open("BeeSolution.txt", "w")

for elem in wdlst:
    outfile.write(elem + '\n')

outfile.close()