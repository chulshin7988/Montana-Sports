
def tax_calculator(subtotal, sales_tax = 0.06):
   tax = round(subtotal * sales_tax, 2)
   total = round(subtotal + tax)
   return [subtotal, tax, total]
