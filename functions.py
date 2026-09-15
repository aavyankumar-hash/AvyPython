def greet_customer():
 print('welcome to the lemonade stand')
 print('fresh jfjfjfjdkjdkdkfj made just for you')

greet_customer()

price_per_cup = float(input('888yw8y8y88w8fy8wf8ywf8ffw8wfwgf8yy'))
cups_sold = int(input('entefrbugbgfdfcgvghiugfgcvb'))

def calculate_total(price, cups):
    total = price * cups
    return total 

total_cost = calculate_total(price_per_cup, cups_sold)

rounded_total = round(total_cost, 2)
print("total cost:",rounded_total)
def  thank_you_message(cups):
    if cups >= 5:
        print("Thank you for your purchase! We appreciate your business and hope to see you again soon.")
    else:
        print("Thank you for your purchase! We hope you enjoy your lemonade and come back for more soon.")
thank_you_message(cups_sold)