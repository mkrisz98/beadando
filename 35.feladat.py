def elofordulasok(string1,string2):
    elofordulas = 0
    x = len(string2)
    for i in range(len(string1)):
        if string1[i:i + x] == string2:
            elofordulas = elofordulas + 1
    return elofordulas
print(elofordulasok("ejifhsdjhgdsghdebrecendshjq dhfdgds dsjfds zebddebrecenh hxz","debrecen"))

