#Ergasia 1
#python 2.7.10
protasi = raw_input("Grapse kati: ")
s=0
i=0
for i in range(len(protasi)):
    s+=1
if (protasi[s-1]!="!"):
    newstr=protasi.replace("!", "")
else:
    newstr=protasi.replace("!", "") + "!"
print newstr
