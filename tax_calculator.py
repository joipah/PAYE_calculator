

Gross_salary=float(input("Enter_Gross_salary:"))
NSSF = 2160
SHIF =Gross_salary * .0275
Housing_levy = Gross_salary * .015
taxable_salary=Gross_salary - NSSF -Housing_levy-SHIF
print("Gross_salary", Gross_salary)
print("NSSF:", NSSF)
print("SHIF:", SHIF)
print("Housing_levy:",  Housing_levy)
print("Taxable_salary:",taxable_salary)

#Above line defines deductions from gross salary
if taxable_salary < 24000:
    tax =taxable_salary * 0.1 -2400
    #above code checks the lower  taxable salary group
elif taxable_salary-24000 <= 8333:
    
    tax= (24000*.1) + (8333 * .25) 
if taxable_salary-32333 <=467667:
    tax= 24000*.1 + (8333) * .25  + (((taxable_salary-32333) * .3))  -2400
elif taxable_salary-(32333 + 467667)  <= 300000:
    tax = 24000*.1 + (8333) * .25   + (467667 *.3) +(taxable_salary -24000 -8333 -467667) * .325 -2400
if taxable_salary-24000*.1 + (8333) * .25   + (467667 *.3) +(taxable_salary -24000 -8333 -467667) * .325 >= 800000:
    tax =24000*.1 + (8333) * .25   + (467667 *.3) +(300000) * .325  + (taxable_salary -24000 -8333 -467667  - 300000) * .35 -2400
if tax   <0.0:
      tax =0.0
Net_salary= taxable_salary-tax
print("Net_salary:" , Net_salary)
print("Tax:", tax)


