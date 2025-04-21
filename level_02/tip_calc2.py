total_bill_amount = float(input("total bill amount? "))
level_of_service = input("level of service: good bad fair ")
split_among_seats = int(input("split among seats "))
good = 0.20
fair = 0.15
bad = 0.10
if level_of_service == "good" : 
    tip = total_bill_amount * good
    total = total_bill_amount + tip
    amount_per_person = total / split_among_seats

    
elif level_of_service == "fair" :
    tip = total_bill_amount * fair
    total = total_bill_amount + tip
    amount_per_person = total / split_among_seats
    
elif level_of_service == "bad" :
    tip = total_bill_amount * bad
    total = total_bill_amount + tip
    amount_per_person = total / split_among_seats
    
print(total_bill_amount)
print(tip)
print(total)
print(amount_per_person)
    
