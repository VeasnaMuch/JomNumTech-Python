print("-" * 50)
number_items = input("Please input number of items that you purhase.")
print("-" * 50)
EXCHANGE_RATE = 4010
invoice = []

i = 0
total_receipt = 0
while (i < int(number_items)):

    items = []
    print(f"{i+1}:")
    print("#" * 50)

    item_name = input ("Product Name : ")
    items.append(item_name)
    item_unit_price = input ("Unit Price : ")
    items.append(item_unit_price)
    item_quantity = input ("Quantity : ")
    items.append(item_quantity)
    item_total_price = float(item_unit_price) * int(item_quantity)
    items.append(item_total_price)    
    total_receipt += item_total_price
    invoice.append (items)
    i +=1


print ("_" * 50, "Your receipt is ready:", sep="\n")
total_vat_10 = total_receipt * 0.1
sub_total = total_receipt + total_vat_10
sub_total_in_khr = sub_total * EXCHANGE_RATE


for item in invoice:
    item_bought = ''
    for i in item:
        item_bought +=  str(i) + "\t"
    print (item_bought)

print ("_" * 50, "\n\n", "Subtotal (USD): ", sub_total, "\n", "Subtotal (KHR): ", sub_total_in_khr)

