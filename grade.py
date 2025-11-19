name = input("Enter student name: ")

m1 = float(input("Enter marks in subject 1: "))
m2 = float(input("Enter marks in subject 2: "))
m3 = float(input("Enter marks in subject 3: "))

if not(0 <= m1 <= 100 and 0 <= m2 <= 100 and 0 <= m3 <= 100):
    print("Error: Marks must be between 0 and 100")
else:
    total = m1 + m2 + m3
    avg = total / 3

    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    elif avg >= 50:
        grade = "C"
    else:
        grade = "D"

    print("Total:", total)
    print("Average:", avg)
    print("Grade:", grade)
