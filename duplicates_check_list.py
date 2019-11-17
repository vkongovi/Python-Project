numbers=[4,34,5,6,7,34,5,6,89,90,1]
unique=[]
for item in numbers:
    if item not in unique:
        unique.append(item)
print(unique)