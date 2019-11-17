customer = {
    "name" :"John Smith",
    "age":"30",
    "is_verified":True
}
print(customer["name"])
print(customer["age"])
#print(customer["birthday"]) --will get key error
#using dictionary.get(key) -- will return if the key name di'dnt match instead of error
Name=customer.get("Name")
print(Name)

#can specifying a default value ot be returned instead of none
Name=customer.get("Name","Agent Smith")
print(Name)
customer["name"]="Ryan"
print(customer)
customer["birthdate"]="01-Jan-1980"
print(customer)