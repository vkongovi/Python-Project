numbers=[4,56,78,2,13,5,92]
largest=0
#print(len(numbers))
for item in numbers:
    if item >= largest:
        largest=item

print(f"Largest is: {largest}")