
import enchant
from itertools import combinations

d = enchant.Dict("en_US")

#instr = ['u', 'a', 'l', 'd', 'y', 'b', 'i']

print("")

totlet = input("How many total letters this week?: ")

totl = int(totlet)

instr = []

for x in range(totl):
    print("")
    letr = input("Please enter one letter, then press enter: ")
    instr.append(letr.lower())

print(""
)
keyletr = input("What is the key letter, please?: ")

print("")

print("Thank you.")

print("")

print("This may take a moment.")

sublst = []

anslst = []

output = sum([list(map(list, combinations(instr, i))) for i in range(len(instr) + 1)], [])

for elem in output:
    if len(elem) > 3:
        sublst.append(elem)

ilist = [0, 1, 2, 3]

itlst = []

tlst = []

x = len(ilist)
y = x**x

for elem in ilist:
    for elem2 in ilist:
        for elem3 in ilist:
            for elem4 in ilist:
                tlst = [elem, elem2, elem3, elem4]
                itlst.append(tlst)



jlist = [0, 1, 2, 3, 4]

fivlst = []

ulst = []

x = len(jlist)
y = x**x

for elem in jlist:
    for elem2 in jlist:
        for elem3 in jlist:
            for elem4 in jlist:
                for elem5 in jlist:
                    ulst = [elem, elem2, elem3, elem4, elem5]
                    fivlst.append(ulst)

klist = [0, 1, 2, 3, 4, 5]

sixlst = []

vlst = []

x = len(klist)
y = x**x

for elem in klist:
    for elem2 in klist:
        for elem3 in klist:
            for elem4 in klist:
                for elem5 in klist:
                    for elem6 in klist:
                        vlst = [elem, elem2, elem3, elem4, elem5, elem6]
                        sixlst.append(vlst)


llist = [0, 1, 2, 3, 4, 5, 6]

sevlst = []

wlst = []

x = len(llist)
y = x**x

for elem in llist:
    for elem2 in llist:
        for elem3 in llist:
            for elem4 in llist:
                for elem5 in llist:
                    for elem6 in llist:
                        for elem7 in llist:
                            wlst = [elem, elem2, elem3, elem4, elem5, elem6, elem7]
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

for elem in outstr:
    if d.check(elem) and keyletr in elem:
        finlst.append(elem)

endlst = []

for elem in finlst:
    if elem not in endlst:
        endlst.append(elem)

print(endlst)

outfile = open("BeeSolution.txt", "w")

for elem in endlst:
    outfile.write(elem + '\n')

outfile.close()