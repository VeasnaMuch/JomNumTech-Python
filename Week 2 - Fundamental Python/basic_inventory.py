APP_NAME = "Inventory Management"
EXCHANGE_RATE = 4010

#Display Header of the application
print('-' * 50) #print character [-] 50 times
print(f"Welcome to the {APP_NAME}!.")
print('-'* 50)

item_name = input("Enter Product Name: ")
item_quantity = input ("Enter Quantity Product: ")
item_unit_price = float(input ("Enter Unit Price: "))
item_total_price_in_usd = int(item_quantity) * float(item_unit_price)
item_total_price_in_riel = item_total_price_in_usd * EXCHANGE_RATE

#Display result
print('-' * 50) #print character [-] 50 times
print(f"Here is your inventory item.")
print('-'* 50)


print(f"Product name : {item_name}" , f"Qty ; {item_quantity}", f"Unit Price : {item_unit_price:.2f}", 
      f"Total in USD : {item_total_price_in_usd : ,.2f}", f"Total in KHR : {item_total_price_in_riel: ,.2f}", 
      sep="\t" )

