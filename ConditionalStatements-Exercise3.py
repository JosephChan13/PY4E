print("Conditional Statements - Exercise 3")

rs = input("Enter Score: ")

try:
    ts = float(rs)

except:
    print("Bad Score")
    quit()

if ts > 1.0:
    print("Bad Score")
    quit()
elif ts >= 0.9:
    print("A")
elif ts >= 0.8:
    print("B")
elif ts >= 0.7:
    print("C")
elif ts >= 0.6:
    print("D")
elif ts < 0.0:
    print("Bad Score")
elif ts < 0.6:
    print("F")

else:
    print("Bad Score")
