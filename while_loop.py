pattern_char='$'
i=1
j=1

while i<=5:
    print('* '* i)
    i=i+1
print('Done')
i=1
j=1
while i <=5:
    j=1
    print()
    while j <=i:
        print(" ",pattern_char,end=" ")
        j+=1
    i+=1
