


has_high_income=True
has_criminal_record=True
has_good_credit=True
#if has_high_income and has_good_credit:
#if has_high_income or has_good_credit:
if has_good_credit and not has_criminal_record:
    print('Eligible for loan')
else:
    print('Sorry ,cannot sanction loan')