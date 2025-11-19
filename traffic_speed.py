speeds = []

for i in range(12):
    value = float(input("Enter speed: "))
    speeds.append(value)

avg_speed = sum(speeds) / len(speeds)

print("Average speed =", avg_speed)

if avg_speed < 40:
    print("Slow")
elif avg_speed <= 80:
    print("Normal")
else:
    print("Fast")
