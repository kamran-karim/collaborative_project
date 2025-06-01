def calculator(a,b):
    choice=input("enter 1 for add, 2 for sub, 3 for multiply, 4 for divide")
    if 'choice'==1:
        print(a+b)
    elif 'choice'==2:
        print(a-b)
    elif 'choice'==3:
        print(a*b)
    elif 'choice'==4:
        print(a/b)
    else:
        print("invalid input")

calculator(2,3)
