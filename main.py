# Tips Calculator
print("Welcome to Tips Calculator")
total_amount = int(input("Enter The Total Bill Amount To be Paid\n"))
no_of_people = int(input("Enter The No of People Paying The Bill \n"))
tips_amount = int(input("Enter How Much Tips You Want to give \n"))
total_bill = total_amount + tips_amount
per_person = (total_amount / no_of_people + tips_amount/no_of_people)
print(f"Total bill Amount will be {total_bill}" + "Rs" )
print(f"Every individual should pay {per_person}" + "Rs")
