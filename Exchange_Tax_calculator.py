
def tax_calculator(subtotal, sales_tax = 0.06):
    """
        takes in a subtotal and tax rate and returns [subtotal, tax, total]
    """
    tax = round(subtotal * sales_tax, 2)
    total = round(subtotal + tax, 2)
    return [subtotal, tax, total]

def currency_converter(price, ex_rate = 0.93):
    return round(price * ex_rate, 2)
