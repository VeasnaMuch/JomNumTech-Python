list_cars = ["Honda", "Toyota", "Ford", "BYD", "Suzuki"]
print("*" * 100)
print(f"Origin list: {list_cars}")

list_cars.insert(0, "Mazda")
print("*" * 100)
print(f"Insert item to the list at index 0: {list_cars}")

list_cars.append("Hyunday")
print("*" * 100)
print(f"Append item to the list at the end: {list_cars}")

list_cars.sort()
print("*" * 100)
print(f"Sorting list: {list_cars}")

item = list_cars.pop(-2)
print("*" * 100)
print(f"Remove item index number 2 from the end: {list_cars}")


