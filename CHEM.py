
cation1list = {"Lithium": "Li^+", "Sodium": "Na^+", "Potassium": "K^+", "Rubidium": "Rb^+", "Cesium": "Cs^+", "Francium": "Fr^+", "Ammonium": "NH4^+", "Copper": "Cu^+", "Hydronium": "H3O^+", "Silver": "Ag^+"}
cation2list = {"Beryllium": "Li^+"}
cation3list = {"Lithium": "Li^+"}
cation4list = {"Lithium": "Li^+"}
cation5list = {"Lithium": "Li^+"}

anion1list = {"Fluoride": "F^-", "Chloride": "Cl^-", "Bromide": "Br^-", "Iodide": "I^-", "Acetate": "C2H3O2^-", "Cyanide": "CN^-", "Hydride": "H^-", "Hydroxide": "OH^-", "Nitrite": "NO2^-", "Nitrate": "NO3^-", "Permanganate": "MnO4^-", "Cyanate": "OCN^-", "Thiocyanate": "SCN^-", "Hypochlorite": "ClO^-", "Chlorite": "ClO2^-", "Chlorate": "ClO3^-", "Perchlorate": "ClO4^-", "Hypobromite": "BrO^-", "Bromite": "BrO2^-", "Bromate": "BrO3^-", "Perbromate": "BrO4^-", "Hypoiodite": "IO^-", "Iodite": "IO2^-", "Iodate": "IO3^-", "Periodate": "IO4^-", "Hydrogen carbonate": "HCO3^-", "Hydrogen sulfite": "HSO3^-", "Hydrogen sulfate": "HSO4^-", "Dihydrogen phosphate": "H2PO4^-"}
anion2list = {"": ""}
anion3list = {"": ""}
anion4list = {"": ""}
anion5list = {"": ""}
anion6list = {"": ""}

def cation1():
    for key in cation1list:
        print("{}: {}".format(key, cation1list[key]))

def cation1():
    for key in cation1list:
        print("{}: {}".format(key, cation1list[key]))

def cation1():
    for key in cation1list:
        print("{}: {}".format(key, cation1list[key]))

def cation1():
    for key in cation1list:
        print("{}: {}".format(key, cation1list[key]))

def cation1():
    for key in cation1list:
        print("{}: {}".format(key, cation1list[key]))



def anion1():
    for key in anion1list:
        print("{}: {}".format(key, anion1list[key]))

def anion2():
    for key in anion2list:
        print("{}: {}".format(key, anion2list[key]))

def anion3():
    for key in anion3list:
        print("{}: {}".format(key, anion3list[key]))

def anion4():
    for key in anion4list:
        print("{}: {}".format(key, anion4list[key]))

def anion5():
    for key in anion5list:
        print("{}: {}".format(key, anion5list[key]))

currentInput = ""#input()
ionlist = {}

while (currentInput != ""):
  inputs = currentInput.split(": ")
  ionlist[inputs[0]] = inputs[1]
  currentInput = input()

print(ionlist)