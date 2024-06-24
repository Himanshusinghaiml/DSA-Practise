def fact(num):
    fact=1
    for  i in range(1,num+1):
        fact=fact*i
    return fact
num=int(input("enter the  int number "))
ans=fact(num)
print("this is our factorial mnumber :", ans)