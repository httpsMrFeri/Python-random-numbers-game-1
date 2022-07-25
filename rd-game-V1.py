import random
num = (random.randrange(1, 10))
num = int(num)
while (True) :
    num1=input("enter random number : ")
    num1=int(num1)
    if num1>num : 
        print ("\n** number is lowest than this **\n")
    elif num1<num :
        print ("\n** number is biger than this **\n")
    elif num1==num :
        print ("\n\n **perfect ** \n\n")
        break
