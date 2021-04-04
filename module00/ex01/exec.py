import sys
#sys.argv retourne les arguments passés sur la  ligne de commande 
#séparateur.join(objets itérables de type str)
merged_words=" ".join(sys.argv[1:])
result=""
for c in merged_words:
    #swapcase pour conversion des lettres
    result=c.swapcase()+result
print(result)
