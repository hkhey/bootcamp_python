import sys 

def text_analyzer(*text):
    if len(text) > 1:
        print("Error")
        return 0
    if len(text) == 1:
        text = list(text)[0]
    if (text==""):
        print("What is the text to analyse?")
        text_analyzer(input())
        return 0
    else:
        characters=0
        upper_case=0
        lower_case=0
        punctuations=0
        spaces = 0
        for i in text:
            characters+=1
            if i.isupper():
                upper_case+=1
            elif i.islower():
                lower_case+=1
            elif i.isspace():
                spaces+=1
            else:
                punctuations+=1
    if(len(sys.argv)>=2):
        print("error")

    print("The text contains", characters," characters:")
    print("- ", upper_case," upper letters\n- ",lower_case," lower letters\n- ", punctuations," punctuation marks\n- ", spaces," space")
