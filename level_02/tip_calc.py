total_bill_amount = float(input("total bill amount? "))
level_of_service = input("level of service: good bad fair ")
good = 0.20
fair = 0.15
bad = 0.10
if level_of_service == "good" : 
    tip = total_bill_amount * good
    total = total_bill_amount + tip

    
elif level_of_service == "fair" :
    tip = total_bill_amount * fair
    total = total_bill_amount + tip
    
elif level_of_service == "bad" :
    tip = total_bill_amount * bad
    total = total_bill_amount + tip

print(total_bill_amount)
print(tip)
print(total)
    
