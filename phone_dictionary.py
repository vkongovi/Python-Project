phone = input("Phone Number:")
digits_mapping={
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine",
    "0":"zero"

}
out_put=""
for char in phone:
    out_put=out_put+digits_mapping.get((char),"!")+" "
print(out_put)