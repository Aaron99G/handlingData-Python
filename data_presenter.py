# Loop through all the data and print each row.
print('///// Step 3 /////')

cupcake_invoices = open('CupcakeInvoices.csv')
for row in cupcake_invoices:
  print(row)

# Loop through all the data and print the type of cupcakes purchased.
print('///// Step 4 /////')

cupcake_invoices = open('CupcakeInvoices.csv')

for row in cupcake_invoices:
  row = row.strip('\n').split(',')
  print(row[2])


# Loop through all the data and print out the total for each invoice (Note: this data is not provided by the csv, you will need to calculate it. Also, keep in mind the data from the csv comes back as a string, you will need to convert it to a float. Research how to do this.).
print('///// Step 5 /////')

cupcake_invoices = open('CupcakeInvoices.csv')

for row in cupcake_invoices:
  row = row.strip('\n').split(',')

  a = float(row[3])
  b = float(row[4])
  total = a * b

  print(total)

# Loop through all the data, and print out the total for all invoices combined.
print('///// Step 6 /////')
cupcake_invoices = open('CupcakeInvoices.csv')

grand_total =0
for row in cupcake_invoices:
  invoice_total = row.strip('\n').split(',')

  a = float(invoice_total[3])
  b = float(invoice_total[4])
  total = a * b
  grand_total = grand_total + total
  
print(round(grand_total,2))
  

# Close your open file.
cupcake_invoices.close()

# Challenge: Do some research and see if you can limit your floats to never exceed two characters after the decimal point.
#Just use round(the_num,how_many_decimals)

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()