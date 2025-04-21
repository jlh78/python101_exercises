day = int(input( 'Day (0-6)? '))
days_of_the_week = list(range(1,6))
#print(days_of_the_week)
weekend = [0,6]

if day in weekend : 
    print("sleep in")
elif day in days_of_the_week :
    print("Go To Work")