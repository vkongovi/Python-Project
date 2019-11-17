#has_good_credit=True
has_good_credit=False
cost_of_house=1000000
if has_good_credit:
    downpayment=0.1*cost_of_house
else:
    downpayment=0.2*cost_of_house

print(f"Your Downpayment is ${downpayment}")