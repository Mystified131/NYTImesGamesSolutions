import enchant

d2 = enchant.DictWithPWL("en_US")

#astr = "This is a text blob to chek to see if it has errors."

print("")

astr = input("Please enter your text to check: ")

wrdlst = astr.split()

errlst = []

suglist = []

ansstr = ""

annstr2 = ""

for elem in wrdlst:
    if not d2.check(elem):
        suglist = d2.suggest(elem)
        ansstr = elem + "-- try instead:"
        for elem2 in suglist:
            ansstr += " " + elem2 + ","
        annstr2 = ansstr[:-1]       

        errlst.append(annstr2)

print("")

print("The spelling errors in this text were: ")

print("")

for elem in errlst:
    print(elem)

## THE GHOST OF THE SHADOW ##

