
import enchant
from itertools import combinations

d = enchant.Dict("en_US")

#instr = ['u', 'a', 'l', 'd', 'y', 'b', 'i']

instr = []

for x in range(7):
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

finlst = []

ilist = [0, 1, 2, 3]

tlst = []

for elem in ilist:
    for elem2 in ilist:
        for elem3 in ilist:
            for elem4 in ilist:
                tlst = [elem, elem2, elem3, elem4]

                for instr in sublst:
                    if len(instr) == 4:  
                        totstr = ""
                        for dlem in tlst:
                            totstr += instr[dlem]
                        if d.check(totstr) and keyletr in totstr and totstr not in finlst:
                            finlst.append(totstr)
                            print(totstr)


jlist = [0, 1, 2, 3, 4]

ulst = []

for elem in jlist:
    for elem2 in jlist:
        for elem3 in jlist:
            for elem4 in jlist:
                for elem5 in jlist:
                    ulst = [elem, elem2, elem3, elem4, elem5]
                    for instr in sublst:
                        if len(instr) == 5:
                            totstr = ""
                            for dlem in ulst:
                                totstr += instr[dlem]
                            if d.check(totstr) and keyletr in totstr and totstr not in finlst:
                                finlst.append(totstr)
                                print(totstr)

                            

klist = [0, 1, 2, 3, 4, 5]

vlst = []


for elem in klist:
    for elem2 in klist:
        for elem3 in klist:
            for elem4 in klist:
                for elem5 in klist:
                    for elem6 in klist:
                        vlst = [elem, elem2, elem3, elem4, elem5, elem6]
                        for instr in sublst:
                            if len(instr) == 6:
                                totstr = ""
                                for dlem in vlst:
                                    totstr += instr[dlem]
                                if d.check(totstr) and keyletr in totstr and totstr not in finlst:
                                    finlst.append(totstr)
                                    print(totstr)

                                

llist = [0, 1, 2, 3, 4, 5, 6]

wlst = []

for elem in llist:
    for elem2 in llist:
        for elem3 in llist:
            for elem4 in llist:
                for elem5 in llist:
                    for elem6 in llist:
                        for elem7 in llist:
                            wlst = [elem, elem2, elem3, elem4, elem5, elem6, elem7]
                            for instr in sublst:
                                if len(instr) == 7:
                                    totstr = ""
                                    for dlem in wlst:
                                        totstr += instr[dlem]
                                    if d.check(totstr) and keyletr in totstr and totstr not in finlst:
                                        finlst.append(totstr)
                                        print(totstr)
                                    


mlist = [0, 1, 2, 3, 4, 5, 6, 7]

xlst = []

for elem in mlist:
    for elem2 in mlist:
        for elem3 in mlist:
            for elem4 in mlist:
                for elem5 in mlist:
                    for elem6 in mlist:
                        for elem7 in mlist:
                            for elem8 in mlist:
                                xlst = [elem, elem2, elem3, elem4, elem5, elem6, elem7, elem8]
                                for instr in sublst:
                                    if len(instr) == 8:
                                        totstr = ""
                                        for dlem in xlst:
                                            totstr += instr[dlem]
                                        if d.check(totstr) and keyletr in totstr and totstr not in finlst:
                                            finlst.append(totstr)
                                            print(totstr)

#nlist = [0, 1, 2, 3, 4, 5, 6, 7, 8]

#ylst = []

#for elem in nlist:
    #for elem2 in nlist:
        #for elem3 in nlist:
            #for elem4 in nlist:
                #for elem5 in nlist:
                    #for elem6 in nlist:
                        #for elem7 in nlist:
                            #for elem8 in nlist:
                                #for elem9 in nlist:
                                    #ylst = [elem, elem2, elem3, elem4, elem5, elem6, elem7, elem8, elem9]
                                    #for instr in sublst:
                                        #if len(instr) == 9:
                                            #totstr = ""
                                            #for dlem in ylst:
                                                #totstr += instr[dlem]
                                            #if d.check(totstr) and keyletr in totstr and totstr not in finlst:
                                                #finlst.append(totstr)
                                                #print(totstr)

#olist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#zlst = []

#for elem in olist:
    #for elem2 in olist:
        #for elem3 in olist:
            #for elem4 in olist:
                #for elem5 in olist:
                    #for elem6 in olist:
                        #for elem7 in olist:
                            #for elem8 in olist:
                                #for elem9 in olist:
                                    #for elem10 in olist:
                                        #zlst = [elem, elem2, elem3, elem4, elem5, elem6, elem7, elem8, elem9, elem10]
                                        #for instr in sublst:
                                            #if len(instr) == 10:
                                                #totstr = ""
                                                #for dlem in zlst:
                                                    #totstr += instr[dlem]
                                                #if d.check(totstr) and keyletr in totstr and totstr not in finlst:
                                                    #finlst.append(totstr)
                                                    #print(totstr)
                                        

print("")

print(finlst)

outfile = open("BeeSolution.txt", "w")

for elem in finlst:
    outfile.write(elem + '\n')

outfile.close()