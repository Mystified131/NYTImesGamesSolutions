import random

print("")

print("Welcome to operation guesser.")

scr = 0

for ctr in range(5):

    print("")

    print("Your score is: ", scr, " out of five.")

    aval = random.randrange(1, 10)
    bval = random.randrange(1, 10)

    opr = random.randrange(5)

    oprlst = [ "addition", "subtraction", "multiplication", "division", "to the power of"]

    ares = int(aval + bval)

    sres = int(aval - bval)

    mres = int(aval * bval)

    dres = int(aval / bval)

    pres = int(aval ^ bval)

    reslst = [ares, sres, mres, dres, pres]

    statres = reslst[opr]

    print("")

    print(aval, " / ", bval, " / ", statres)

    print("")

    print("What operation makes the first two numbers result in the whole number value of the third?")

    print("")

    oprin = input("Press 0 for addition, 1 for subtraction, 2 for multiplication, 3 for division and 4 for to the power of: ")

    print("")

    opin = int(oprin)

    if opin < 0 or opin > 4:
        opin = 0

    plastres = reslst[opin]

    anslst = []

    for elem in reslst:
        if plastres == elem:
            anslst.append(opin)

    resstr = oprlst[opin]

    if opin in anslst:

        print("You guessed ", resstr, " which is correct.")

        scr += 1

    if opin not in anslst:

        print("You guessed ", resstr, " which is not correct.")

print("")

print("Your total score is: ", scr, " out of 5 possible. Thank you for playing.")



    