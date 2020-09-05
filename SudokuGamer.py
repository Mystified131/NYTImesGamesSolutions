import datetime

puzl = [[0, 2, 0, 5, 0, 0, 8, 7, 6],
[7, 0, 0, 1, 8, 0, 0, 5, 0],
[8, 5, 9, 7, 0, 0, 0, 4, 0],
[5, 9, 0, 0, 0, 4, 6, 8, 1],
[0, 1, 0, 0, 3, 0, 0, 0, 0],
[0, 0, 0, 8, 6, 0, 0, 9, 5],
[2, 0, 7, 0, 0, 8, 0, 0, 9],
[9, 0, 4, 0, 0, 7, 2, 0, 8],
[0, 0, 0, 0, 0, 2, 4, 6, 0]]

a = []

for elem in puzl:
    a.append(elem)

suba = []

subb = []

for x in range(9):
    suba = []
    for x2 in range(9):
        if ((puzl)[x][x2]) != 0:
            suba.append((puzl)[x][x2])

    subb.append(suba)

subc = []

subd = []

for y in range(9):
    subc = []
    for x in range(9):
        if ((puzl)[x][y]) != 0:
            subc.append((puzl)[x][y])

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
                apt = puzl[x2][y2]
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

for x in range(9):
    subh = []
    for y in range(9):
        subj = []
        if puzl[x][y] != 0:
            subj.append(puzl[x][y])
            subh.append(subj)
        if puzl[x][y] == 0:
            subh.append(subf[x][y])
        tup = tuple(subh)

    subi.append(tup)

for pitr in range(1000):

    right_now = datetime.datetime.now().isoformat()
    tlist = []

    for i in right_now:
        if i.isnumeric():
            tlist.append(i)

    tim = ("".join(tlist))

    print(subi)

    print("")

    print("Your puzzle:")

    print("")

    for elemq in a:
        print(elemq)

    print("")

    print("")

    xv = int(input("Please enter the row of the new value (0-8): "))

    print("")

    xy = int(input("Please enter the column of the new value (0-8): "))

    print("")

    xval = int(input("Please enter the new value: "))

    if xval in subi[xv][xy]:

        a[xv][xy] = xval

        print("")

        print("Your puzzle:")

        print("")

        for elemq in a:
            print(elemq)

        print("")

    if xval not in subi[xv][xy]:

        print("")

        print("That value would create a discrepancy in row, column or sub grid, or conflicts with an original puzzle value.")

        print("")


    ctr = 0

    for elemy in a:
        for elemz in elemy:
            if elemz != 0:
                ctr += 1
    
    if ctr == 80:

        break

if ctr == 80:

    print("")

    print("Congratulations! Your puzzle has been solved.")

    print("")

    print("Good work!")


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