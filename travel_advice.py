distance = float(input("Enter how far you want to travel (in miles): "))

if distance < 3:
    print("Ride Bicycle")
elif distance < 300:
    print("Ride Motor-Cycle")
else:
    print("Drive Super-Car")
