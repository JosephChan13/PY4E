print("Iterations - Exercise 2")

count = 0
sum = 0.0
minimum = None
maximum = None

while True :
    ed = input("Enter a number: ")
    if ed == "done" :
        break
    try:
        fd = float(ed)
    except:
        print("Invalid input")
        continue

    count = count + 1
    sum = sum + fd

    udata = fd
    for data in [udata] :
        if minimum is None :
            minimum = data
        elif data < minimum :
            minimum = data

    udata = fd
    for data in [udata] :
        if maximum is None :
            maximum = data
        elif data > maximum :
            maximum = data

print("Total:", sum, "Count:", count, "Maximum:", maximum, "Minimum:", minimum)
