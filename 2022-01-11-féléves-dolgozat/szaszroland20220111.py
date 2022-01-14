import random
#############

# 001-es feladat
print("001-es feladat")
#----------------------

name = str(input("\nAdd meg a neved> "))
print(name , ", üdvözöllek nállunk!")



# 002-es feladat
print("002-es feladat")
#----------------------

bYear = int(input("\nAdd meg a születési éved> "))
calculate = 2022 - bYear
print(calculate)



# 003-as feladat
print("003-as feladat")
#----------------------

num = int(input("\nAdd meg, hogy mennyit keresel> "))
minimalber = 260000

if num < minimalber:
    print("Alacsony")
elif num == minimalber:
    print("Kielégítő")
elif num > minimalber:
    print("Magas")



# 004-es feladat
print("004-es feladat")
#----------------------

vezeteknev = str(input("\nAdd meg a VEZEVEZETÉKNEVED> "))
keresztnev = str(input("Add meg a KERESZTNEVED> "))
szemelyi = int(input("Add meg a személyi igazolvány számodat> "))
datum = int(input("Add meg a kitöltés dátumát> "))
osszeg = int(input("Add meg, hogy mennyit keresel> "))

print("\n===========================================")
print("Vezetéknév:", vezeteknev , "|" , "Keresztnév:" , keresztnev)
print("-------------------------------------------")
print("Személyi igazolvány szám:" , szemelyi)
print("-------------------------------------------")
print("Összeg:" , osszeg , "Ft")
print("===========================================")
print(datum)



# 005-ös feladat
print("005-ös feladat")
#----------------------
print("")#csak hogy szépebb legyen :D
for x in range(10, 0, -1):
    print(x)




# 006-os feladat
print("006-os feladat")
#----------------------
print("")#csak hogy szépebb legyen :D
for i in range(10, 0, -1):
    if i %2 != 0:
        print(i)



# 007-es feladat
print("007-es feladat")
#----------------------
print("")#csak hogy szépebb legyen :D
for i in range(1, 11):
    if i %2 == 0:
        print(i)



# 008-as feladat
print("008-as feladat")
#----------------------

userChoice = str(input("\nFej vagy Írás? (Kisbetű fontos!)> "))
choices = ["fej" , "írás"]
coin = random.choice(choices)

if coin == userChoice:
    print("Eltaláltad")
else:
    print("Majd talán másokor összejön :D !")



# 009-es feladat
print("009-es feladat")
#----------------------

print("\nJó napod van? (Lehetséges válaszok : igen , nem)")
x = input(">>> ")

if x == "igen":
    print("Akkor csak így tovább :) !")
elif x == "nem":
    print("Ülj le egy fél órára, csináld amit szeretsz és légy azokkal akiket szeretsz, és lásd mindjárt jobb lész!")



# 009a feladat
print("009a feladat")
#----------------------

if x != "igen":
    print("Sajnos nem értem a válaszod")
elif x != "nem":
    print("Sajnos nem értem a válaszod")



# 010-es feladat
print("010-es feladat")
#----------------------

nums = []
for i in range(1,6):
    nums.append(i)
mChoice = random.choice(nums)

guess = int(input("\nTippelj milyen számra gondoltam 1 és 5 között?> "))

if guess == mChoice:
    print("Eltaláltad")
else:
    print("Ez most nem jött össze!")