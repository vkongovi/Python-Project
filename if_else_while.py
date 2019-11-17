num=int(input("Enter the value of n"))
if (num<=0):
    print("Enter a valid value for n")
else:
    sum=0
    while (num>0):
        sum+=num
        num-=1


print(sum)