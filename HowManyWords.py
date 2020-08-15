import enchant
from itertools import combinations
from PyDictionary import PyDictionary

dictionary=PyDictionary()

d = enchant.Dict("en_US")

sublst = []

#wlist = ["s", "a", "t", "c", "h", "e", "l"]

print("")

print("Please enter 7 letters: ")

wlist = []

for x in range(7):
    print("")
    letr = input("Please enter one letter, then press enter: ")
    wlist.append(letr.lower())

print("")

print("Thank you.")

print("")

print("This may take a moment.")

print("")

output = sum([list(map(list, combinations(wlist, i))) for i in range(len(wlist) + 1)], [])

for elem in output:
    if len(elem) == 7:
        sublst.append(elem)

llist = [0, 1, 2, 3, 4, 5, 6]

sevlst = []

wlst = []

for elem in llist:
    for elem2 in llist:
        for elem3 in llist:
            for elem4 in llist:
                for elem5 in llist:
                    for elem6 in llist:
                        for elem7 in llist:
                            wlst = [elem, elem2, elem3, elem4, elem5, elem6, elem7]
                            #if len(set(wlst)) == 7:
                            sevlst.append(wlst)

outstr = []

for instr in sublst:

    if len(instr) == 4:

        for elem in itlst:

            totstr = ""

            for elem2 in elem:
                totstr += instr[elem2]
            outstr.append(totstr)

    if len(instr) == 5:

        for elem3 in fivlst:

            totstr = ""

            for elem4 in elem3:
                totstr += instr[elem4]
            outstr.append(totstr)

    if len(instr) == 6:

        for elem6 in sixlst:

            totstr = ""

            for elem7 in elem6:
                totstr += instr[elem7]
            outstr.append(totstr)

    if len(instr) == 7:

        for elem8 in sevlst:

            totstr = ""

            for elem9 in elem8:
                totstr += instr[elem9]
            outstr.append(totstr)

finlst = []

synlst = []

for elem in outstr:
    if d.check(elem):
        sylst = dictionary.synonym(elem)

        try:
            finm = elem + "-- like: " + str(sylst[0])

        except:
            finm = elem

        finlst.append(finm)

endlst = []

for elem in finlst:
    if elem not in endlst:
        endlst.append(elem)

print("")

for elem in endlst:
    print(elem)

outfile = open("HowManyWords.txt", "w")

for elem in endlst:
    outfile.write(elem + '\n')

outfile.close()

