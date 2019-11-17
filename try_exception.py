try:
    age=int(input("Age:"))
    income = 30000
    risk=income / age
    print(age)
    print("Risk factor is:"+str(risk))
except ZeroDivisionError:
    print("Age cannot be zero")
except ValueError:
    print("Invalid value for age")