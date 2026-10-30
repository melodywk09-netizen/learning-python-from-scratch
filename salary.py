"""
develop a payment calculator
prompt the user to enter rate per hour
number of hours worked
total pay
if the total pay is>= $5000 deduct 10% to tax VAT
else deduct 4%
display total pay before and after deduction
"""

Full_name=str(input("Full Name:"))
Department=str(input("Department:"))
Pay=int(input("Pay Per Hour:"))
Hours=int(input("Hours worked per week:"))
Total= Pay*Hours
print("Pay before VAT", Total)
if Total>5000 :
    print("Total after 10% VAT=", Total*0.10)
else:
 print("Total after 4% VAT=", Total*0.40)

