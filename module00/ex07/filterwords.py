import sys
import re
if (len(sys.argv)<3 or len(sys.argv)>3):
    print("ERROR")
text=sys.argv[1]
n=sys.argv[2]
if (text.isdigit() or n.isalpha()):
    print("ERROR")
else:
    R=[]
    #findall(expression à matcher,text danslequel on doit rechercher)
    #\w tous les alphanum de a à z et de 0 à 9 et les _ sont recherchés 
    #le prefixe r /exempple:'\n' designe new line alors que r'\n' designe ddeux caractères
    #+ nombre de caractères attendus est 1 ou plus
    L=re.findall(r'\w+',text)
    for i in L:
        if(len(i)>int(n)):
            R.append(i)
    print(R)
