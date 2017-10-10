def tabuada():
    tab = 0
    while tab < 10:
        tab = tab + 1
        i = 0
        while i < 10:
            i = i + 1
            print (tab, "x", i, "=", tab*i)
        print()

#tabuada()

# ok
def tabuada2():
    tab = 1
    while tab <= 10:
        i = 1
        while i <= 10:
            print(tab,"x",i,"=",tab*i)
            i = i + 1
        print()
        tab = tab + 1

#tabuada2()

# errada 
def tabuada3():
    tab = 1
    i = 1
    while tab <= 10 and i <= 10:
        print(tab,"x",i,"=",tab*i)
        i = i + 1
        tab = tab + 1
    print()

#tabuada3()

#ok
def tabuada4():
    tab = 1
    while tab <= 10:
        i = 1
        while i <= 10:
            print(tab*i, end = "\t")
            i = i + 1
        print()
        tab = tab + 1

tabuada4()
#errada
def tabuada5():
    tab = 1
    while tab <= 10:
        i = 1
        print(tab*i, end = "\t")
        i = i + 1
        print()
        tab = tab + 1

tabuada5()