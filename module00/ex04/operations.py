import sys
length=len(sys.argv)
if(length==1):
    print("Usage: python operations.py <number1> <number2>\nExample:\n  python operations.py 10 3")
if(length==3):
    x=sys.argv[1]
    y=sys.argv[2]
    if(x.isalpha() or y.isalpha()):
        print("InputError: only numbers")
    else:
        x=int(x)
        y=int(y)
        print("Sum:        ",x+y)
        print("Differnce:  ",x-y)
        print("Product:    ",x*y)
        if(y==0):
            print("ERROR(div by zero)")
            print("ERROR(modulo by zero)")
        else:
            print("Quotient:   ",x/y)
            print("Remainder   ",x%y)
if(length>3):
    print("InputError: too many arguments\nUsage: python operations.py <number1> <number2>\nExample:\n  python operations.py 10 3")
