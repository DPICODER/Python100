# Building a python code for calculating tip among people for a bill

print("Tip Calculator !")

bill = float(input("Enter total bill :"))

tip = int(input("Enter the tip Percentage : 10 , 12, 15 "))

ppl = int(input("No of people splitting Bill :"))

bilL_with_tip = tip/100 * bill+ bill

bill_per_person = bilL_with_tip / ppl

final_amt = round(bill_per_person ,2)

print(f"Each has to pay {final_amt}")


