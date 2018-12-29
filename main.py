import sys, os, time


def mainmen():
    print("here is some of the file you can take and they will do serten thing")
    print(" 1. make file \n 2. delet files \n 3. chooes directory")
    c = input("chooes witch one you want [1, 2, 3]? ")


    if c == "1":
        print("you will be redirected to the ""make file part"" ")
        if time.sleep(2) == time.sleep(2):
            print("loading")
            time.sleep(2)
        lol()
    elif c == "2":
        print("you will be redirected to the ""delet file part"" ")
        if time.sleep(2) == time.sleep(2):
            print("loading")
            time.sleep(2)
        delet()
    elif c == "3":
        print("you will be redirected to the ""chooes directery part"" ")
        if time.sleep(2) == time.sleep(2):
            print("loading")
            time.sleep(2)
        chooesdir()

def chooesdir():
    print("you are at the choose dir part.")


def lol():
    global i
    i = input("pls insert your file name here")


    f = open(i + ".txt", "w")
    #f.write("hello this is the file we created.")
    printfile = input("do you want to print something to the file? ")
    if printfile == "yes":
        awnseryes = input("what do you want to print to the file? ")
        with open(i +".txt", "w", ) as f:
            f.write(awnseryes)

        with open(i+".txt", "r") as r:
            b = r.read()
            if b == "hello there":
                bb = input("you are a starwars fan? ")
                if bb == "yes":
                    print("that is great mate here is your esteregg")

                    if time.sleep(2) == time.sleep(2):
                        print("loading")
                        time.sleep(2)
                    theegg()
            else:
                if time.sleep(2) == time.sleep(2):
                    print("loading")
                    time.sleep(2)
                mainmen()

    elif printfile == "no":
        print("okay we will tansport you to the other functions")
        if time.sleep(2) == time.sleep(2):
            print("loading")
            time.sleep(2)
        delet()
    else:
        print("that was not right you will now be exited")
        sys.exit()

    yes = input("do you want to take the file off your system? ")
    if yes == "yes":
        print("your file will be delated soon.")
        if time.sleep(2) == time.sleep(2):
            print("loading")
            time.sleep(2)
        delet()
    elif yes == "no":
        print("okay then, we will send you to the start again")
        if time.sleep(2) == time.sleep(2):
            print("loading")
            time.sleep(2)
        lol()
    else:
        print("that was not right")
        print(yes)


def delet():
    ii = input("what file do you want to delet? (you do not need to set the .exempel)")
    os.remove(ii + ".txt")
    i = input("do you want to delet another file? ")


    if i == "yes":
        print("you will soon be redirected to the delet agean.")
        if time.sleep(2) == time.sleep(2):
            print("loading")
            time.sleep(2)
        delet()
    elif i == "no":
        print("you will be redicteded to the main part of the file")
        if time.sleep(2) == time.sleep(2):
            print("loading")
            time.sleep(2)
        mainmen()



def exit():
    g = input("are you sure you want to exit this application? ")
    if g == "yes":
        print("okay we will exit the aplication soon.")
        time.sleep(2)
        sys.exit()
    elif g == "no":
        print("okay we will send you to the start")
        time.sleep(2)
        lol()
    else:
        print("you need to awnser yes or on on the question")
        time.sleep(2)
        exit()




def theegg():
    with open(i +".txt", "w") as f:
        f.write("this is the egg you wanted :)")
    os.system("start "+i+".txt")




mainmen()
