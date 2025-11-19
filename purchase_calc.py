filename = input("Enter purchase file name: ")

items = 0
free_items = 0
amount = 0
discount = 0

with open(filename, "r") as f:
    for line in f:
        line = line.strip()

        if line == "":
            continue

        parts = line.split()

        # If line ends with Free
        if parts[-1].lower() == "free":
            free_items += 1

        # If line starts with Discount
        elif parts[0].lower() == "discount":
            discount = float(parts[1])

        # Otherwise, It's a paid item 
        else:
            price = float(parts[-1])
            items += 1
            amount += price


final_amount = amount - discount

print("No of items purchased:", items)
print("No of free items:", free_items)
print("Amount to pay:", amount)
print("Discount given:", discount)
print("Final amount paid:", final_amount)