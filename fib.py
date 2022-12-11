# Program to predict whether an entered number is in fibonacci series or not
#generating fibonacci series
def fib(num):
    f1 = 0
    f2 = 1
    flag = 0
    while f1<=num:
        if f1==num or f2==num:
            flag = 1
        f3 = f1 + f2
        f1 = f2
        f2 = f3
    if flag==1:
        print("The entered value is Valid")
    else:
        print("The entered value is Invalid")

#Fetching the number of digits to be checked
n = int(input("Enter the number of elements to be searched: "))

#checking if the entered numbers are Valid or Not
for i in range(0,n):
    num = int(input("Enter the number: "))
    fib(num)