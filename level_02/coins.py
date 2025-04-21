coins = 0
print(f"you have {coins} coins ")
number_of_coins = input("do you want another coin? ")
while True :
    if number_of_coins == "yes" :
        coins += 1 
        print(coins) 
        number_of_coins = input("do you want another coin? ")
    else : 
        print("bye")
        exit()





