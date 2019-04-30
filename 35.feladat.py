string1 = "ejifhsdjhgdsghdebrecendshjq dhfdgds dsjfds zebddebrecenh hxz"
string2 = "debrecen"
elofordulas = 0
x = len(string2)
for i in range(len(string1)):
    if string1[i:i+x] == string2:
        elofordulas = elofordulas + 1
print("String2 előfordulása String1-ben:",elofordulas)