elements = "H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Uut Fl Mc Lv Ts Og".split()

# Returns a list containing the elements that can be found in a word
def getElements(word):
    eList = []
    for i in range(len(word)):
        if i < len(word)-1:
            c = word[i+1]  
        else: # we are on the last letter, a single letter
            c = ""
        d = word[i]+c
        if word[i].title() in elements:
            eList.append(word[i].title())
        if len(d) == 2:
            if d.title() in elements:
                eList.append(d.title())
    return eList


# try combinations of els to make WORD.
def combo(storage, data):
    for i in range(len(data)):
        if len(storage) > 0:
            if storage[0][0].lower() not in WORD[0].lower():
                break
        new_storage = storage[:]
        new_data = data[:]
        new_storage.append(data[i])
        new_data = data[i+1:]
        new_word = "".join(new_storage)
        if new_word.lower() == WORD :
            results.append(new_word)
        combo(new_storage,new_data)
    return results


results = [] # global list to store the results
WORD = 'bacon'
els = getElements(WORD)
print(combo([], els))
