import random
num1 = input("enter renge of number \n enter min number : ")
min = int(num1)
num2 = input("enter max number : ")
max = int(num2)

num = input("enter number : ")
r_num =(random.randrange(min,max))
funk = input (str(r_num)+" is your number or no ?? \nyes this is my number(1)\tno my number is bigger than this(2)\tno my number is lowest than this(3) : ")
if funk == "1":
    print("\n\nNICE\n\n")
    exit()
elif funk == "2" :
    while (r_num < max):
        r_num=r_num+1
        n1 = input (str(r_num)+" this is your number ? \n yes(1)\tno(2) : ")
        if n1 == "1":
            print("\n\nNICE\n\n")
            exit()
        elif n1 == 2 :
            print("lest go to find it")
elif funk == "3" :
    while (r_num > min):
        r_num=r_num-1
        n1 = input (str(r_num)+" this is your number ? \n yes(1)\tno(2) : ")
        if n1 == "1":
            print("\n\nNICE\n\n")
            exit()
        elif n1 == 2 :
            print("lest go to find it")