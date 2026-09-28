"""
num=int(input("enter the number"))
if num>=0:
    if num%2==0:
        print("positive even")
    else:
        print("negative odd")
else:
    print("negative number")            

mark=int(input("enter the mark"))
if mark>=35:
    if mark>=90:
        print("A grade")
    elif mark>=80 and mark<90:
        print("B grade")
    elif mark>=50 and mark<80:
        print("C grade")
    elif mark<=35 and mark<50:
        print("D grade")

else:
    print("fail")                
    """
    #program to find bank transation deta
balance=50000
amount=int(input("enter the number"))
atmpass=int(input("enter pin"))
if atmpass==1234:
        if amount<=balance:
            balance=balance-amount
            print("balance=",balance)
            print("Transation successfull")
        else:
            print("not transation") 
else:
    print("insuffient bank balance")           