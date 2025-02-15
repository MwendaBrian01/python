#this is an an electicity bill calculator

customerID = int(input("Enter your customer ID: "))
customerName =str(input("Enter your Customer Name: "))  
unitConsumed = float(input("Enter the total units you have consumed: "))


if unitConsumed <= 199:
    charges_per_unit = 1.20
elif 200 <= unitConsumed < 400:  
    charges_per_unit = 1.50
elif 400 <= unitConsumed < 600:
    charges_per_unit = 1.80
else:  # Greater than or equal to 600
    charges_per_unit = 2.00

# Calculate total bill
total_bill = unitConsumed * charges_per_unit


if total_bill > 400:  
    surcharge = total_bill * 0.15  
    total_bill += surcharge  
else:
    surcharge = 0  


if total_bill < 100:
    total_bill = 100

# Display results
print("\nTHIS IS THE TOTAL BILL")
print("----------------------------")
print(f"Customer ID      : {customerID}")
print(f"Customer Name    : {customerName}")
print(f"Units Consumed   : {unitConsumed}")
print(f"Charges per Unit : Ksh {charges_per_unit:.2f}")
print(f"Surcharge Amount : Ksh {surcharge:.2f}")
print(f"Total Amount to Pay : Ksh {total_bill:.2f}")
print("\nTHANK FOR CHOOSING OUR ELECTRICITY CALCULATOR")
print("----------------------------")
