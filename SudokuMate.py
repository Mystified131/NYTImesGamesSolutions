from itertools import  permutations
import random
import datetime

print("")

levv = input("Please enter '0' for an Easy Puzzle, '1' for a Medium Puzzle or '2' for a Hard Puzzle: ")

print("")

quant = 1

print("One moment, please.")

levl = int(levv)

if levl == 0 or levl == 1 or levl == 2:
    lev = levl
if levl < 0 or levl > 2:
    lev = 0

print("")

bulk = 0

while bulk < quant:

    right_now = datetime.datetime.now().isoformat()
    tlist = []

    for i in right_now:
        if i.isnumeric():
            tlist.append(i)

    tim = ("".join(tlist))

    alist = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    worm = list(permutations(alist, 9))

    totnum = len(worm)

    anum = random.randrange(totnum)

    list1 = []

    for elem in worm[anum]:

        list1.append(elem)

    worklist = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    word = list(permutations(worklist, 9))

    list2 = []

    if len(list1) > 8:

        for elem in word:

            if elem[0] != list1[0] and elem[1] != list1[1] and elem[2] != list1[2] and elem[3] != list1[3] and elem[4] != list1[4] and elem[5] != list1[5] and elem[6] != list1[6] and elem[7] != list1[7] and elem[8] != list1[8]:
                if elem[0] != list1[0] and elem[0] != list1[1] and elem[0] != list1[2]:
                    if elem[1] != list1[0] and elem[1] != list1[1] and elem[1] != list1[2]:
                        if elem[2] != list1[0] and elem[2] != list1[1] and elem[2] != list1[2]:
                            if elem[3] != list1[3] and elem[3] != list1[4] and elem[3] != list1[5]:
                                if elem[4] != list1[3] and elem[4] != list1[4] and elem[4] != list1[5]:
                                    if elem[5] != list1[3] and elem[5] != list1[4] and elem[5] != list1[5]:
                                        if elem[6] != list1[6] and elem[6] != list1[7] and elem[6] != list1[8]:
                                            if elem[7] != list1[6] and elem[7] != list1[7] and elem[7] != list1[8]:
                                                if elem[8] != list1[6] and elem[8] != list1[7] and elem[8] != list1[8]:

                                                    for elem2 in elem:
                                                        list2.append(elem2)

                                                if len(list2) > 8:

                                                    break

        if len(list2) > 8:

            list3 = []

            for elem in word:

                if elem[0] != list1[0] and elem[1] != list1[1] and elem[2] != list1[2] and elem[3] != list1[3] and elem[4] != list1[4] and elem[5] != list1[5] and elem[6] != list1[6] and elem[7] != list1[7] and elem[8] != list1[8]:
                    if elem[0] != list2[0] and elem[1] != list2[1] and elem[2] != list2[2] and elem[3] != list2[3] and elem[4] != list2[4] and elem[5] != list2[5] and elem[6] != list2[6] and elem[7] != list2[7] and elem[8] != list2[8]:
                        if elem[0] != list1[0] and elem[0] != list1[1] and elem[0] != list1[2]:
                            if elem[1] != list1[0] and elem[1] != list1[1] and elem[1] != list1[2]:
                                if elem[2] != list1[0] and elem[2] != list1[1] and elem[2] != list1[2]:
                                    if elem[3] != list1[3] and elem[3] != list1[4] and elem[3] != list1[5]:
                                        if elem[4] != list1[3] and elem[4] != list1[4] and elem[4] != list1[5]:
                                            if elem[5] != list1[3] and elem[5] != list1[4] and elem[5] != list1[5]:
                                                if elem[6] != list1[6] and elem[6] != list1[7] and elem[6] != list1[8]:
                                                    if elem[7] != list1[6] and elem[7] != list1[7] and elem[7] != list1[8]:
                                                        if elem[8] != list1[6] and elem[8] != list1[7] and elem[8] != list1[8]: 
                                                            if elem[0] != list2[0] and elem[0] != list2[1] and elem[0] != list2[2]:     
                                                                if elem[1] != list2[0] and elem[1] != list2[1] and elem[1] != list2[2]:
                                                                    if elem[2] != list2[0] and elem[2] != list2[1] and elem[2] != list2[2]:
                                                                        if elem[3] != list2[3] and elem[3] != list2[4] and elem[3] != list2[5]:
                                                                            if elem[4] != list2[3] and elem[4] != list2[4] and elem[4] != list2[5]:
                                                                                if elem[5] != list2[3] and elem[5] != list2[4] and elem[5] != list2[5]:
                                                                                    if elem[6] != list2[6] and elem[6] != list2[7] and elem[6] != list2[8]:
                                                                                        if elem[7] != list2[6] and elem[7] != list2[7] and elem[7] != list2[8]:
                                                                                            if elem[8] != list2[6] and elem[8] != list2[7] and elem[8] != list2[8]:              
                                                                                                
                                                                                                for elem2 in elem:
                                                                                                    list3.append(elem2)

                                                                                            if len(list3) > 8:

                                                                                                break

            if len(list3) > 8:                                                                                    

                list4 = []

                for elem in word:

                    if elem[0] != list1[0] and elem[1] != list1[1] and elem[2] != list1[2] and elem[3] != list1[3] and elem[4] != list1[4] and elem[5] != list1[5] and elem[6] != list1[6] and elem[7] != list1[7] and elem[8] != list1[8]:
                        if elem[0] != list2[0] and elem[1] != list2[1] and elem[2] != list2[2] and elem[3] != list2[3] and elem[4] != list2[4] and elem[5] != list2[5] and elem[6] != list2[6] and elem[7] != list2[7] and elem[8] != list2[8]:
                            if elem[0] != list3[0] and elem[1] != list3[1] and elem[2] != list3[2] and elem[3] != list3[3] and elem[4] != list3[4] and elem[5] != list3[5] and elem[6] != list3[6] and elem[7] != list3[7] and elem[8] != list3[8]:
                        
                                for elem2 in elem:
                                    list4.append(elem2)

                            if len(list4) > 8:

                                break

                if len(list4) > 8:

                    list5 = []

                    for elem in word:

                        if elem[0] != list1[0] and elem[1] != list1[1] and elem[2] != list1[2] and elem[3] != list1[3] and elem[4] != list1[4] and elem[5] != list1[5] and elem[6] != list1[6] and elem[7] != list1[7] and elem[8] != list1[8]:
                            if elem[0] != list2[0] and elem[1] != list2[1] and elem[2] != list2[2] and elem[3] != list2[3] and elem[4] != list2[4] and elem[5] != list2[5] and elem[6] != list2[6] and elem[7] != list2[7] and elem[8] != list2[8]:
                                if elem[0] != list3[0] and elem[1] != list3[1] and elem[2] != list3[2] and elem[3] != list3[3] and elem[4] != list3[4] and elem[5] != list3[5] and elem[6] != list3[6] and elem[7] != list3[7] and elem[8] != list3[8]:
                                    if elem[0] != list4[0] and elem[1] != list4[1] and elem[2] != list4[2] and elem[3] != list4[3] and elem[4] != list4[4] and elem[5] != list4[5] and elem[6] != list4[6] and elem[7] != list4[7] and elem[8] != list4[8]:
                                        if elem[0] != list4[0] and elem[0] != list4[1] and elem[0] != list4[2]:
                                            if elem[1] != list4[0] and elem[1] != list4[1] and elem[1] != list4[2]:
                                                if elem[2] != list4[0] and elem[2] != list4[1] and elem[2] != list4[2]:
                                                    if elem[3] != list4[3] and elem[3] != list4[4] and elem[3] != list4[5]:
                                                        if elem[4] != list4[3] and elem[4] != list4[4] and elem[4] != list4[5]:
                                                            if elem[5] != list4[3] and elem[5] != list4[4] and elem[5] != list4[5]:
                                                                if elem[6] != list4[6] and elem[6] != list4[7] and elem[6] != list4[8]:
                                                                    if elem[7] != list4[6] and elem[7] != list4[7] and elem[7] != list4[8]:
                                                                        if elem[8] != list4[6] and elem[8] != list4[7] and elem[8] != list4[8]:

                                                                            for elem2 in elem:
                                                                                list5.append(elem2)

                                                                        if len(list5) > 8:

                                                                            break

                    if len(list5) > 8:

                        list6 = []

                        for elem in word:

                            if elem[0] != list1[0] and elem[1] != list1[1] and elem[2] != list1[2] and elem[3] != list1[3] and elem[4] != list1[4] and elem[5] != list1[5] and elem[6] != list1[6] and elem[7] != list1[7] and elem[8] != list1[8]:
                                if elem[0] != list2[0] and elem[1] != list2[1] and elem[2] != list2[2] and elem[3] != list2[3] and elem[4] != list2[4] and elem[5] != list2[5] and elem[6] != list2[6] and elem[7] != list2[7] and elem[8] != list2[8]:
                                    if elem[0] != list3[0] and elem[1] != list3[1] and elem[2] != list3[2] and elem[3] != list3[3] and elem[4] != list3[4] and elem[5] != list3[5] and elem[6] != list3[6] and elem[7] != list3[7] and elem[8] != list3[8]:
                                        if elem[0] != list4[0] and elem[1] != list4[1] and elem[2] != list4[2] and elem[3] != list4[3] and elem[4] != list4[4] and elem[5] != list4[5] and elem[6] != list4[6] and elem[7] != list4[7] and elem[8] != list4[8]:
                                            if elem[0] != list5[0] and elem[1] != list5[1] and elem[2] != list5[2] and elem[3] != list5[3] and elem[4] != list5[4] and elem[5] != list5[5] and elem[6] != list5[6] and elem[7] != list5[7] and elem[8] != list5[8]:
                                                if elem[0] != list4[0] and elem[0] != list4[1] and elem[0] != list4[2]:
                                                    if elem[1] != list4[0] and elem[1] != list4[1] and elem[1] != list4[2]:
                                                        if elem[2] != list4[0] and elem[2] != list4[1] and elem[2] != list4[2]:
                                                            if elem[3] != list4[3] and elem[3] != list4[4] and elem[3] != list4[5]:
                                                                if elem[4] != list4[3] and elem[4] != list4[4] and elem[4] != list4[5]:
                                                                    if elem[5] != list4[3] and elem[5] != list4[4] and elem[5] != list4[5]:
                                                                        if elem[6] != list4[6] and elem[6] != list4[7] and elem[6] != list4[8]:
                                                                            if elem[7] != list4[6] and elem[7] != list4[7] and elem[7] != list4[8]:
                                                                                if elem[8] != list4[6] and elem[8] != list4[7] and elem[8] != list4[8]: 
                                                                                    if elem[0] != list5[0] and elem[0] != list5[1] and elem[0] != list5[2]:     
                                                                                        if elem[1] != list5[0] and elem[1] != list5[1] and elem[1] != list5[2]:
                                                                                            if elem[2] != list5[0] and elem[2] != list5[1] and elem[2] != list5[2]:
                                                                                                if elem[3] != list5[3] and elem[3] != list5[4] and elem[3] != list5[5]:
                                                                                                    if elem[4] != list5[3] and elem[4] != list5[4] and elem[4] != list5[5]:
                                                                                                        if elem[5] != list5[3] and elem[5] != list5[4] and elem[5] != list5[5]:
                                                                                                            if elem[6] != list5[6] and elem[6] != list5[7] and elem[6] != list5[8]:
                                                                                                                if elem[7] != list5[6] and elem[7] != list5[7] and elem[7] != list5[8]:
                                                                                                                    if elem[8] != list5[6] and elem[8] != list5[7] and elem[8] != list5[8]:              
                                                                                                
                                                                                                                        for elem2 in elem:
                                                                                                                            list6.append(elem2)

                                                                                                                    if len(list6) > 8:

                                                                                                                        break

                        if len(list6) > 8:

                            list7 = []

                            for elem in word:

                                if elem[0] != list1[0] and elem[1] != list1[1] and elem[2] != list1[2] and elem[3] != list1[3] and elem[4] != list1[4] and elem[5] != list1[5] and elem[6] != list1[6] and elem[7] != list1[7] and elem[8] != list1[8]:
                                    if elem[0] != list2[0] and elem[1] != list2[1] and elem[2] != list2[2] and elem[3] != list2[3] and elem[4] != list2[4] and elem[5] != list2[5] and elem[6] != list2[6] and elem[7] != list2[7] and elem[8] != list2[8]:
                                        if elem[0] != list3[0] and elem[1] != list3[1] and elem[2] != list3[2] and elem[3] != list3[3] and elem[4] != list3[4] and elem[5] != list3[5] and elem[6] != list3[6] and elem[7] != list3[7] and elem[8] != list3[8]:
                                            if elem[0] != list4[0] and elem[1] != list4[1] and elem[2] != list4[2] and elem[3] != list4[3] and elem[4] != list4[4] and elem[5] != list4[5] and elem[6] != list4[6] and elem[7] != list4[7] and elem[8] != list4[8]:
                                                if elem[0] != list5[0] and elem[1] != list5[1] and elem[2] != list5[2] and elem[3] != list5[3] and elem[4] != list5[4] and elem[5] != list5[5] and elem[6] != list5[6] and elem[7] != list5[7] and elem[8] != list5[8]:
                                                    if elem[0] != list6[0] and elem[1] != list6[1] and elem[2] != list6[2] and elem[3] != list6[3] and elem[4] != list6[4] and elem[5] != list6[5] and elem[6] != list6[6] and elem[7] != list6[7] and elem[8] != list6[8]:
                                            
                                                        for elem2 in elem:
                                                            list7.append(elem2)

                                                    if len(list7) > 8:

                                                        break

                            if len(list7) > 8:

                                list8 = []

                                for elem in word:

                                    if elem[0] != list1[0] and elem[1] != list1[1] and elem[2] != list1[2] and elem[3] != list1[3] and elem[4] != list1[4] and elem[5] != list1[5] and elem[6] != list1[6] and elem[7] != list1[7] and elem[8] != list1[8]:
                                        if elem[0] != list2[0] and elem[1] != list2[1] and elem[2] != list2[2] and elem[3] != list2[3] and elem[4] != list2[4] and elem[5] != list2[5] and elem[6] != list2[6] and elem[7] != list2[7] and elem[8] != list2[8]:
                                            if elem[0] != list3[0] and elem[1] != list3[1] and elem[2] != list3[2] and elem[3] != list3[3] and elem[4] != list3[4] and elem[5] != list3[5] and elem[6] != list3[6] and elem[7] != list3[7] and elem[8] != list3[8]:
                                                if elem[0] != list4[0] and elem[1] != list4[1] and elem[2] != list4[2] and elem[3] != list4[3] and elem[4] != list4[4] and elem[5] != list4[5] and elem[6] != list4[6] and elem[7] != list4[7] and elem[8] != list4[8]:
                                                    if elem[0] != list5[0] and elem[1] != list5[1] and elem[2] != list5[2] and elem[3] != list5[3] and elem[4] != list5[4] and elem[5] != list5[5] and elem[6] != list5[6] and elem[7] != list5[7] and elem[8] != list5[8]:
                                                        if elem[0] != list6[0] and elem[1] != list6[1] and elem[2] != list6[2] and elem[3] != list6[3] and elem[4] != list6[4] and elem[5] != list6[5] and elem[6] != list6[6] and elem[7] != list6[7] and elem[8] != list6[8]:
                                                            if elem[0] != list7[0] and elem[1] != list7[1] and elem[2] != list7[2] and elem[3] != list7[3] and elem[4] != list7[4] and elem[5] != list7[5] and elem[6] != list7[6] and elem[7] != list7[7] and elem[8] != list7[8]:
                                                                if elem[0] != list7[0] and elem[0] != list7[1] and elem[0] != list7[2]:
                                                                    if elem[1] != list7[0] and elem[1] != list7[1] and elem[1] != list7[2]:
                                                                        if elem[2] != list7[0] and elem[2] != list7[1] and elem[2] != list7[2]:
                                                                            if elem[3] != list7[3] and elem[3] != list7[4] and elem[3] != list7[5]:
                                                                                if elem[4] != list7[3] and elem[4] != list7[4] and elem[4] != list7[5]:
                                                                                    if elem[5] != list7[3] and elem[5] != list7[4] and elem[5] != list7[5]:
                                                                                        if elem[6] != list7[6] and elem[6] != list7[7] and elem[6] != list7[8]:
                                                                                            if elem[7] != list7[6] and elem[7] != list7[7] and elem[7] != list7[8]:
                                                                                                if elem[8] != list7[6] and elem[8] != list7[7] and elem[8] != list7[8]:
                                                                
                                                                                                    for elem2 in elem:
                                                                                                        list8.append(elem2)

                                                                                                if len(list8) > 8:

                                                                                                    break

                                if len(list8) > 8:

                                    list9 = []

                                    for elem in word:

                                        if elem[0] != list1[0] and elem[1] != list1[1] and elem[2] != list1[2] and elem[3] != list1[3] and elem[4] != list1[4] and elem[5] != list1[5] and elem[6] != list1[6] and elem[7] != list1[7] and elem[8] != list1[8]:
                                            if elem[0] != list2[0] and elem[1] != list2[1] and elem[2] != list2[2] and elem[3] != list2[3] and elem[4] != list2[4] and elem[5] != list2[5] and elem[6] != list2[6] and elem[7] != list2[7] and elem[8] != list2[8]:
                                                if elem[0] != list3[0] and elem[1] != list3[1] and elem[2] != list3[2] and elem[3] != list3[3] and elem[4] != list3[4] and elem[5] != list3[5] and elem[6] != list3[6] and elem[7] != list3[7] and elem[8] != list3[8]:
                                                    if elem[0] != list4[0] and elem[1] != list4[1] and elem[2] != list4[2] and elem[3] != list4[3] and elem[4] != list4[4] and elem[5] != list4[5] and elem[6] != list4[6] and elem[7] != list4[7] and elem[8] != list4[8]:
                                                        if elem[0] != list5[0] and elem[1] != list5[1] and elem[2] != list5[2] and elem[3] != list5[3] and elem[4] != list5[4] and elem[5] != list5[5] and elem[6] != list5[6] and elem[7] != list5[7] and elem[8] != list5[8]:
                                                            if elem[0] != list6[0] and elem[1] != list6[1] and elem[2] != list6[2] and elem[3] != list6[3] and elem[4] != list6[4] and elem[5] != list6[5] and elem[6] != list6[6] and elem[7] != list6[7] and elem[8] != list6[8]:
                                                                if elem[0] != list7[0] and elem[1] != list7[1] and elem[2] != list7[2] and elem[3] != list7[3] and elem[4] != list7[4] and elem[5] != list7[5] and elem[6] != list7[6] and elem[7] != list7[7] and elem[8] != list7[8]:
                                                                    if elem[0] != list8[0] and elem[1] != list8[1] and elem[2] != list8[2] and elem[3] != list8[3] and elem[4] != list8[4] and elem[5] != list8[5] and elem[6] != list8[6] and elem[7] != list8[7] and elem[8] != list8[8]:
                                                                        if elem[0] != list7[0] and elem[0] != list7[1] and elem[0] != list4[2]:
                                                                            if elem[1] != list7[0] and elem[1] != list7[1] and elem[1] != list7[2]:
                                                                                if elem[2] != list7[0] and elem[2] != list7[1] and elem[2] != list7[2]:
                                                                                    if elem[3] != list7[3] and elem[3] != list7[4] and elem[3] != list7[5]:
                                                                                        if elem[4] != list7[3] and elem[4] != list7[4] and elem[4] != list7[5]:
                                                                                            if elem[5] != list7[3] and elem[5] != list7[4] and elem[5] != list7[5]:
                                                                                                if elem[6] != list7[6] and elem[6] != list7[7] and elem[6] != list7[8]:
                                                                                                    if elem[7] != list7[6] and elem[7] != list7[7] and elem[7] != list7[8]:
                                                                                                        if elem[8] != list7[6] and elem[8] != list7[7] and elem[8] != list8[8]: 
                                                                                                            if elem[0] != list8[0] and elem[0] != list8[1] and elem[0] != list8[2]:     
                                                                                                                if elem[1] != list8[0] and elem[1] != list8[1] and elem[1] != list8[2]:
                                                                                                                    if elem[2] != list8[0] and elem[2] != list8[1] and elem[2] != list8[2]:
                                                                                                                        if elem[3] != list8[3] and elem[3] != list8[4] and elem[3] != list8[5]:
                                                                                                                            if elem[4] != list8[3] and elem[4] != list8[4] and elem[4] != list8[5]:
                                                                                                                                if elem[5] != list8[3] and elem[5] != list8[4] and elem[5] != list8[5]:
                                                                                                                                    if elem[6] != list8[6] and elem[6] != list8[7] and elem[6] != list8[8]:
                                                                                                                                        if elem[7] != list8[6] and elem[7] != list8[7] and elem[7] != list8[8]:
                                                                                                                                            if elem[8] != list8[6] and elem[8] != list8[7] and elem[8] != list8[8]:          

                                                                                                                                                for elem2 in elem:
                                                                                                                                                    list9.append(elem2)

                                                                                                                                            if len(list9) > 8:

                                                                                                                                                break

                                    if len(list9) > 8:

                                        totsod = []

                                        totsod.append(list1)
                                        totsod.append(list2)
                                        totsod.append(list3)
                                        totsod.append(list4)
                                        totsod.append(list5)
                                        totsod.append(list6)
                                        totsod.append(list7)
                                        totsod.append(list8)
                                        totsod.append(list9)

                                        if lev == 0:
                                            remnum = 41
                                        if lev == 1:
                                            remnum = 51
                                        if lev == 2:
                                            remnum = 56

                                        remlst = []

                                        for x in range(81):
                                            x1 = random.randrange(9)
                                            y1 = random.randrange(9)

                                            loclist = (x1, y1)

                                            if loclist not in remlst:
                                                remlst.append(loclist)

                                            if len(remlst) == remnum:
                                                break

                                        checkl = []

                                        subl = []
                                        endl = []

                                        for x in range(9):
                                            subl = []
                                            for y in range(9):
                                                
                                                checkl = (x, y)

                                                if checkl in remlst:

                                                    aval = 0

                                                if checkl not in remlst:

                                                    aval = int(totsod[x][y])

                                                subl.append(aval)

                                            endl.append(subl)

                                        print("")

                                        bulky = bulk + 1

                                        for x in range(9):
                                            print(endl[x])

                                        titstr = "SodokuCreator." + tim + ".txt"

                                        outfile = open(titstr, "w")

                                        if lev == 0:
                                            levstr = "Level: Easy"
                                        if lev == 1:
                                            levstr = "Level: Medium"
                                        if lev == 2:
                                            levstr = "Level: Hard"

                                        astr = "Viable Sodoku Instance-- Created: " + tim

                                        outfile.write(astr + '\n')
                                        outfile.write("" + '\n')
                                        outfile.write (levstr + '\n')
                                        outfile.write("" + '\n')

                                        for elem in totsod:

                                            outfile.write(elem[0] + "  "  + elem[1] + "  "  + elem[2] + "  "  + elem[3] + "  "  + elem[4] + "  "  + elem[5] + "  "  + elem[6] + "  "  + elem[7] + "  "  + elem[8] + "  "  + '\n')

                                        outfile.close()

                                        if len(list1) < 8 or len(list2) < 8 or len(list3) < 8 or len(list4) < 8 or len(list5) < 8 or len(list6) < 8 or  len(list7) < 8 or len(list8) < 8 or len(list9) < 8:
                                        
                                            bulk == bulk

                                        else:

                                            bulk += 1

print("")

print("See the solution document in the same folder as your code.")

print("")

puzl = []

for elem in (endl):
    puzl.append(elem)

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

    print("")

    print("Your puzzle:")

    print("")

    for elemq in a:
        print(elemq)

    print("")

    print("")

    xv = int(input("Please enter the row of the new value (0-8): "))

    if xv < 0:
        xv = 0

    if xv > 8:
        xv = 8

    print("")

    xy = int(input("Please enter the column of the new value (0-8): "))

    if xv < 0:
        xv = 0

    if xy > 8:
        xy = 8

    print("")

    xval = int(input("Please enter the new value: "))

    ychk = []

    for yv in range(9):
        ychk.append(a[yv][xv])

    if xval in subi[xv][xy] and xval not in a[xy] and xval not in ychk:

        a[xv][xy] = xval

    else:

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

            




