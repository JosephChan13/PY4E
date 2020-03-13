print("Iterations - Exercise 1")

count = 0
sum = 0.0

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

print(sum,count,sum/count)
