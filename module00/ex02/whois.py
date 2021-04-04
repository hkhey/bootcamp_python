import sys
parameters=sys.argv
if len(parameters)>2:
    print('Error')
else:
    number=parameters[1]
    if number.isdigit():
        if(int(number)==0):
            print("I\'m zero")
        elif(int(number)%2==0):
            print("I\'m even")
        else:
            print("I\'m Odd")
    else:
        print("Error")
