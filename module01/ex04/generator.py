import random
def generator(text, sep, option=None):
    if not isinstance(text, str):
        print("Error")
        return
    if option is not None:
        if(option == "shuffle"):
            L=text.split()
            R=[]
            random_list = random.sample(range(0, len(L)), len(L))
            for i in random_list:
                R.append(L[i])
            return R
        if(option == "unique"):
            L=text.split()
            R=[]
            random_list = random.sample(range(0, len(L)), len(L))
            for i in random_list:
                R.append(L[i])
            S=set(R)
            return S            
        if(option == "ordered"):
            L=text.split()
            Ordered=sorted(L)
            return Ordered
    else:
        print("ok")
text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" ", option="ordered"):
    print(word)