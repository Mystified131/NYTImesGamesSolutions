import enchant
from itertools import permutations
import random
from subprocess import call
import datetime

right_now = datetime.datetime.now().isoformat()
tlist = []

for i in right_now:
    if i.isnumeric():
        tlist.append(i)

tim = ("".join(tlist))

d = enchant.Dict("en_US")

conlst = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z"]
vowlst = ["A",  "E",  "I", "O", "U", "Y"]

oplst = []

letlst = []

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

for x1 in range(12):
    astr = sublst[x1]
    oplst.append(astr)

#print("")

#print(oplst)

letlst.append([oplst[0], oplst[1], oplst[2]])
letlst.append([oplst[3], oplst[4], oplst[5]])
letlst.append([oplst[6], oplst[7], oplst[8]])
letlst.append([oplst[9], oplst[10], oplst[11]])

print("")

print("Please be patient. The possibilties may take some minutes to generate. If the original configuration fails, the code will re-run. Thank you.")

print("")

print(letlst)

print("")

letdict = {}

for x in range(12):
    astr = oplst[x]
    y = int((x/3) + 1)

    letdict[astr] = y

#print(letdict)

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

print("Master word list generated.")

subs = []

r = len(letlst)

print("")
print("Working through possible solutions (this may take a moment):")
print("")
#print(letlst)
#print("")

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

                                        #print ([elem, elem2, elem3])

                                        print("Generating possible answers. Please wait. . .")

                                        print("")

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

#print(subs)

if subs:
    print("Answers generated.")

if not subs:
    print("Trying again!")
    print("")
    call(["python", "LetterBoxedPlay.py"])

titstr = "LetterBoxedSolution." + tim + ".txt"

outfile = open(titstr, "w")

outfile.write ("A Tenable Letter Boxed Solution." + '\n' )
outfile.write ("" + '\n' )
outfile.write ("Time: " + tim + '\n')
outfile.write ("" + '\n' )

for elem in oplst:
    outfile.write(elem + ",")

outfile.write('\n')
outfile.write ("" + '\n' )

for elem2 in subs:
    outfile.write(elem2[0] + ", " + elem2[1] + ", " + elem2[2] + '\n')

outfile.close()

print("")

print("See the solution document in the same folder as your code.")

print("")

for ctr in range(1000):

    print("")

    print(letlst)

    print("")

    gssstr1 = input("Please enter your first of three guess words: ")

    print("")

    gssstr2 = input("Please enter your second of three guess words: ")

    print("")

    gssstr3 = input("Please enter your third of three guess words: ")

    print("")

    win = 0

    for elem in subs:

        if gssstr1.lower() == elem[0].lower() and gssstr2.lower() == elem[1].lower() and gssstr3.lower() == elem[2].lower():

            print("A winner!")

            print("")

            win += 1

    if win == 0:

        print("Not in our calculated 3-word list. Sorry.")

        print("")

    outstr = input("Press q to quit or anything else to continue: ")

    print("")

    if outstr == "q":

        break

## THE GHOST OF THE SHADOW ##




