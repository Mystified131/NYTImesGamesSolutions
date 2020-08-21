import enchant
from itertools import permutations
import datetime

right_now = datetime.datetime.now().isoformat()
tlist = []

for i in right_now:
    if i.isnumeric():
        tlist.append(i)

tim = ("".join(tlist))

d = enchant.Dict("en_US")

oplst = []

letlst = []

for x in range(12):
    print("")
    letr = input("Please enter one letter, in order per side, then press enter: ")
    oplst.append(letr.lower())

letlst.append([oplst[0], oplst[1], oplst[2]])
letlst.append([oplst[3], oplst[4], oplst[5]])
letlst.append([oplst[6], oplst[7], oplst[8]])
letlst.append([oplst[9], oplst[10], oplst[11]])

print("")

print("Please be patient. The possibilties may take some minues to generate. Thank you.")

print("")

print(letlst)

print("")

letdict = {}

for x in range(12):
    astr = oplst[x]
    y = int((x/3) + 1)
    letdict[astr] = y

print(letdict)

wdlst = []

worl = list(permutations(oplst, 3))
worm = list(permutations(oplst, 4))
worn = list(permutations(oplst, 5))
woro = list(permutations(oplst, 6))

wor = ""

for elem in worl:

    astr = ""
    
    for wor in elem:
        astr += wor

    if d.check(astr) and astr not in wdlst:

        wdlst.append(astr)

for elem in worm:

    astr = ""

    for wor in elem:
        astr += wor

    if d.check(astr) and astr not in wdlst:

        wdlst.append(astr)


for elem in worn:

    astr = ""

    for wor in elem:
        astr += wor

    if d.check(astr) and astr not in wdlst:

        wdlst.append(astr)

for elem in woro:

    astr = ""

    for wor in elem:
        astr += wor

    if d.check(astr) and astr not in wdlst:

        wdlst.append(astr)

print("")

print(wdlst)

subs = []

r = len(letlst)

print("")
print("Possible solutions (this may take a moment):")
print("")
print("Most work, but check for modern parlance:")
print("")

for elem in wdlst:
    for elem2 in wdlst:
        for elem3 in wdlst:
            if elem[-1] == elem2[0] and elem2[-1] == elem3[0]:
                if [elem, elem2, elem3] not in subs:  

                    z = 0 

                    j = len(elem)

                    for k in range(j - 1):

                        kstr = elem[k]
                        kkstr = elem[k + 1]

                        if letdict[kstr] == letdict[kkstr]:

                            z = 1

                    s = 0 

                    j2 = len(elem2)

                    for k2 in range(j2 - 1):

                        kstr2 = elem2[k2]
                        kkstr2 = elem2[k2 + 1]

                        if letdict[kstr2] == letdict[kkstr2]:

                            s = 1                       

                    kk = 0

                    j3 = len(elem3)

                    for k3 in range(j3 - 1):

                        kstr3 = elem3[k3]
                        kkstr3 = elem3[k3 + 1]

                        if letdict[kstr3] == letdict[kkstr3]:

                            kk = 1   

                    
                    if not z:

                        if not s:

                            if not kk:

                                letlst = []

                                for ltr in elem:

                                    letlst.append(ltr)     

                                for ltr in elem2:

                                    letlst.append(ltr)

                                for ltr in elem3:

                                    letlst.append(ltr)

                                letset = set(letlst)

                                litset = list(letset)

                                q = all(x in litset for x in oplst)

                                if q:

                                    if len(litset) == 12:

                                        print ([elem, elem2, elem3])

                                        subs.append([elem, elem2, elem3])


#for elem in wdlst:
    #for elem2 in wdlst:
        #for elem3 in wdlst:
            #for elem4 in wdlst:
                #if elem[-1] == elem2[0] and elem2[-1] == elem3[0] and elem3[-1] == elem4[0]:
                    #if ([elem, elem2, elem3, elem4]) not in subs:

                        #z = 0 

                        #j = len(elem)

                        #for k in range(j - 1):

                            #kstr = elem[k]
                            #kkstr = elem[k + 1]

                            #if letdict[kstr] == letdict[kkstr]:

                                #z = 1

                        #s = 0 

                        #j2 = len(elem2)

                        #for k2 in range(j2 - 1):

                            #kstr2 = elem2[k2]
                            #kkstr2 = elem2[k2 + 1]

                            #if letdict[kstr2] == letdict[kkstr2]:

                                #s = 1                       

                        #kk = 0

                        #j3 = len(elem3)

                        #for k3 in range(j3 - 1):

                            #kstr3 = elem3[k3]
                            #kkstr3 = elem3[k3 + 1]

                            #if letdict[kstr3] == letdict[kkstr3]:

                                #kk = 1   

                        #kl = 0

                        #j4 = len(elem4)

                        #for k4 in range(j4 - 1):

                            #kstr4 = elem4[k4]
                            #kkstr4 = elem4[k4 + 1]

                            #if letdict[kstr4] == letdict[kkstr4]:

                                #kl = 1   

                        #if not z:

                            #if not s:

                                #if not kk:

                                    #if not kl:

                                        #letlst = []

                                        #for ltr in elem:

                                            #letlst.append(ltr)

                                        #for ltr in elem2:

                                            #letlst.append(ltr)

                                        #for ltr in elem3:

                                            #letlst.append(ltr)

                                        #for ltr in elem4:

                                            #letlst.append(ltr)

                                        #letset = set(letlst)

                                        #litset = list(letset)

                                        #q = all(x in litset for x in oplst)

                                        #if q:

                                            #if len(litset) == 12:
                
                                                #print ([elem, elem2, elem3, elem4])
   
                                                #subs.append([elem, elem2, elem3, elem4])


print("")

print(subs)

titstr = "LetterBoxedSolution." + tim + ".txt"

outfile = open(titstr, "w")

for elem in subs:
    outfile.write(elem[0] + ", " + elem[1] + ", " + elem[2] + '\n')

outfile.close()




