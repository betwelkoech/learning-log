tea = 30
ndazi = 20

no_tea=int(input("Enter number of cups of tea: "))
no_ndazi=int(input("Enter number of ndazi of tea: "))
total = no_tea*tea + no_ndazi*ndazi
print("The Total bill is: ", total)

if total<200:
    print("THis is a small bill")
else:
    print("Print You must be rich")

print("PAYMENT SCTIONB")
paid=int(input("Enter Amount Paid"))
bal= paid-total
print("BALANCE: ", bal)

