#BILL CALCULATOR

#ASK FOR THE NUMBER OF PEOPLE --> Check if datatype is valid (integer)
while True:
    try:
        num_of_people = int(input("Number of People: "))
    except:
        print("Invalid input, please try again")
        print()
        continue
    else:
        break

#VALIDATE DATA --> If the number of people is less than or equal to 0, report that it's an invalid input and ask for another input
while num_of_people <= 0:
    print("Invalid input, please try again.")
    print()
    num_of_people = int(input("Number of People: "))

#ASK FOR THE TOTAL BILL --> Check if datatype is valid (float/integer)
while True:
    try:
        bill_total = float(input("Total Bill: "))
    except:
        print("Invalid input, please try again")
        print()
        continue
    else:
        break

#VALIDATE DATA --> If the bill_total is less than 0, report that it's an invalid input and ask for another input
while bill_total <= 0:
    print("Invalid input, please try again")
    print()
    bill_total = float(input("Total Bill: "))

#ASK IF THE USER WANTS TO USE NYC TAX TO CALCULATE THE BILL --> If not, ask the user to input a different tax
tax = str.upper(input("Would you like to use the NYC tax rate(0.08875)? (YES/NO): "))

#VALIDATE THE INPUT(YES/NO) --> If invalid, report that it's an invalid input and ask for another input
while tax != "YES" and tax != "NO":
    print("Invalid input, please try again.")
    print()
    tax = str.upper(input("Would you like to use the NYC tax rate? (YES/NO): "))

#If the input is YES, use the NYC sales tax rate (8.875%)
#If the input is NO, ask the user to input another sales tax rate and use that rate instead
if tax == "YES":
    tax = 0.08875
else:
    tax = float(input("Enter tax rate (in decimal format): "))

#ASK FOR TIP AMOUNT
while True:
    try:
        tip = float(input("Enter tip amount: "))
    except:
        print("Invalid input, please try again")
        print()
        continue
    else:
        break

#For each person, ask how many dishes the person had
#For each dish the person had, ask the price of the dish and add up the total value of all dishes that person had
total_all = 0
total_list = []

for i in range(1, num_of_people + 1):
    while True:
        try:
            print()
            num_dishes = int(input(f"Number of dishes person #{i} had: "))
        except:
            print("Invalid input, please try again")
            print()
            continue
        else:
            break

    total_price_dish = 0
    for j in range(1, num_dishes + 1):
        while True:
            try:
                price_dish = float(input(f"Price of dish #{j}: "))
            except:
                print("Invalid input, please try again")
                print()
                continue
            else:
                break
        total_price_dish = total_price_dish + price_dish
        total_price_dish_after_tax = total_price_dish * (1 + tax)
    total_all = total_all + total_price_dish

    total_list.append(total_price_dish_after_tax + (tip/num_of_people)) #keep track of the total per person 

    print(f"Total price of dishes for person #{i}: ${format(total_price_dish, '.2f')}")
    print(f"Total price of dishes for person #{i} AFTER TAX: ${format(total_price_dish_after_tax, '.2f')}")
    print(f"Total price of dishes for person #{i} AFTER TAX + TIPS: ${format(total_price_dish_after_tax + (tip/num_of_people), '.2f')}")

print()
print("----------")
print("FINAL REPORT")
print()
for i in range(1, len(total_list) + 1):
    print("Grand total for person #" + str(i) + ": $" + format(total_list[i-1], '.2f'))
print()

#CALCULATE GRAND TOTAL
grand_total = 0
for i in total_list:
    grand_total += i

print("PROVIDED Grand Total:", format(bill_total, '.2f'))
print(f"CALCULATED Grand Total: ${format(grand_total, '.2f')}")
print()