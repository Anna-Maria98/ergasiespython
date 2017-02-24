#Ergasia 3
#python 2.7.10
pinakas = []
total = int(raw_input("Sunolo stoixeiwn: "))
for i in range(total):
    lista = int(raw_input("Arithmos: "))
    pinakas.append(lista)
pinakas_2 = []

s=0
for i in range(len(pinakas)):
    if (pinakas[i]!=0):
        pinakas_2.append(pinakas[i])
    else:
        s+=1
for i in range(s):
    pinakas_2.append(0)
print pinakas
print pinakas_2
