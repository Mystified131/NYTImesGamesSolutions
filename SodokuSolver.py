import datetime

right_now = datetime.datetime.now().isoformat()
tlist = []

for i in right_now:
    if i.isnumeric():
        tlist.append(i)

tim = ("".join(tlist))

a = []

b = [(1, 2, 3, 4, 5, 6, 7, 8, 9)]

#for x1 in range(9):

    #shlst = []

    #for x in range(9):
        #print("")
        #numr = input("Please enter one number, in order, then press enter. For blanks please enter a zero: ")
        #shlst.append(int(numr))

    #a.append(shlst)

a = [[0, 2, 0, 5, 0, 0, 8, 7, 6],
 [7, 0, 0, 1, 8, 0, 0, 5, 0],
 [8, 5, 9, 7, 0, 0, 0, 4, 0],
 [5, 9, 0, 0, 0, 4, 6, 8, 1],
 [0, 1, 0, 0, 3, 0, 0, 0, 0],
 [0, 0, 0, 8, 6, 0, 0, 9, 5],
 [2, 0, 7, 0, 0, 8, 0, 0, 9],
 [9, 0, 4, 0, 0, 7, 2, 0, 8],
 [0, 0, 0, 0, 0, 2, 4, 6, 0]]


print("")

print("Your entry:")

print("")

print(a)

print("")

print("The solution should appear quite rapidly or not at all, depending on your processor strength.")

print("")

suba = []

subb = []

for x in range(9):
    suba = []
    for x2 in range(9):
        if ((a)[x][x2]) != 0:
            suba.append((a)[x][x2])

    subb.append(suba)

subc = []

subd = []

for y in range(9):
    subc = []
    for x in range(9):
        if ((a)[x][y]) != 0:
            subc.append((a)[x][y])

    subd.append(subc)

sube = []

subf = []

alst = []

sett = []

subsett = []

for x in range(3):
    for y in range(3):
        subsett = []
        for x1 in range(3):
            for y1 in range(3):
                x2 = (x * 3) + x1
                y2 = (y * 3) + y1
                apt = a[x2][y2]
                if apt != 0:
                    subsett.append(apt)
        sett.append(subsett)

refset = [[1, 1, 1, 2, 2, 2, 3, 3, 3],
[1, 1, 1, 2, 2, 2, 3, 3, 3],
[1, 1, 1, 2, 2, 2, 3, 3, 3],
[4, 4, 4, 5, 5, 5, 6, 6, 6],
[4, 4, 4, 5, 5, 5, 6, 6, 6],
[4, 4, 4, 5, 5, 5, 6, 6, 6],
[7, 7, 7, 8, 8, 8, 9, 9, 9],
[7, 7, 7, 8, 8, 8, 9, 9, 9], 
[7, 7, 7, 8, 8, 8, 9, 9, 9]]

for x in range(9):
    sube = []
    for y in range(9):
        neglst = []
        c = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for elem in subb[x]:
            neglst.append(elem)
        for elem2 in subd[y]:
            neglst.append(elem2)

        ss = (refset[x][y]) -1

        for elem3 in sett[ss]:
 
            neglst.append(elem3)

        negst = list(set(neglst))

        for elem3 in negst:
            c.remove(elem3)

        sube.append(c)

    subf.append(sube)

subh = []

subi = []

subj = []

for x in range(9):
    subh = []
    for y in range(9):
        subj = []
        if a[x][y] != 0:
            subj.append(a[x][y])
            subh.append(subj)
        if a[x][y] == 0:
            subh.append(subf[x][y])
        tup = tuple(subh)

    subi.append(tup)

perma = []

subx = []

vlst = []

for x in range(9):
    subx = []
    y = 0
 
    for elem in subi[x][y]:
        for elem2 in subi[x][y+1]:
            for elem3 in subi[x][y+2]:
                for elem4 in subi[x][y+3]:
                    for elem5 in subi[x][y+4]:
                        for elem6 in subi[x][y+5]:
                            for elem7 in subi[x][y+6]:
                                for elem8 in subi[x][y+7]:
                                   
                                    for elem9 in subi[x][y+8]:

                                        ulst = []
                                        slst = []

                                        err = 0

                                        nsum = elem  + elem2 + elem3 + elem4 + elem5 + elem6 + elem7 + elem8 + elem9

                                        if nsum != 45:

                                            err = 1

                                        if err < 1: 
                
                                            slst.append(elem)
                                            slst.append(elem2)
                                            slst.append(elem3)
                                            slst.append(elem4)
                                            slst.append(elem5)
                                            slst.append(elem6)
                                            slst.append(elem7)
                                            slst.append(elem8)
                                            slst.append(elem9)
                                        


                                        ulst = list(set(slst))
                                        if len(ulst) > 8:
                                            if slst not in subx:
                                                batman = tuple(slst)

                                                subx.append(batman)

    vlst = list(set(subx))

    supman = tuple(vlst)
    perma.append(supman)                                            

 ###############################################

totposs = []

for elem in perma[0]:
    for elem2 in perma[1]:
        for elem3 in perma[2]:
            for elem4 in perma[3]:
                for elem5 in perma[4]:
                    for elem6 in perma[5]:
                        for elem7 in perma[6]:
                            for elem8 in perma[7]:
                                for elem9 in perma[8]:

                                    subm = []
                                    ulist = []
                                 
                                    err = 0

                                    for y in range(9):
                                        nsum = elem[y]  + elem2[y] + elem3[y] + elem4[y] + elem5[y] + elem6[y] + elem7[y] + elem8[y] + elem9[y]

                                        if nsum != 45:

                                            err = 1

                                    if err < 1: 

                                        subm.append(elem)
                                        subm.append(elem2)
                                        subm.append(elem3)
                                        subm.append(elem4)
                                        subm.append(elem5)
                                        subm.append(elem6)
                                        subm.append(elem7)
                                        subm.append(elem8)
                                        subm.append(elem9)
                                                
                                        totposs.append(subm)

lensol = ""
lensol = str(len(totposs))

print("Possible Answer(s): " + lensol)

print("")

for elem in totposs:
    for x in range(9):
        print(elem[x])
    print("")

print(""
)
## THE GHOST OF THE SHADOW ##

a = [[0, 2, 0, 5, 0, 0, 8, 7, 6],
 [7, 0, 0, 1, 8, 0, 0, 5, 0],
 [8, 5, 9, 7, 0, 0, 0, 4, 0],
 [5, 9, 0, 0, 0, 4, 6, 8, 1],
 [0, 1, 0, 0, 3, 0, 0, 0, 0],
 [0, 0, 0, 8, 6, 0, 0, 9, 5],
 [2, 0, 7, 0, 0, 8, 0, 0, 9],
 [9, 0, 4, 0, 0, 7, 2, 0, 8],
 [0, 0, 0, 0, 0, 2, 4, 6, 0]]

a = [[0, 0, 1, 7, 0, 0, 5, 0, 0],
 [0, 0, 7, 2, 4, 0, 0, 0, 0],
 [0, 4, 0, 0, 1, 8, 9, 0, 7],
 [0, 6, 0, 0, 0, 0, 0, 0, 8],
 [0, 0, 9, 0, 2, 0, 0, 1, 0],
 [7, 0, 8, 0, 5, 6, 2, 0, 0],
 [0, 0, 0, 0, 0, 0, 4, 3, 0],
 [0, 0, 0, 0, 0, 0, 6, 0, 0],
 [5, 0, 6, 0, 0, 0, 0, 0, 0]]

