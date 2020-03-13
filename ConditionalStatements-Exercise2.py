print("Conditional Statements - Exercise 2")

ah = input("Enter Hours: ")
ar = input("Enter Rate: ")

try:
    bh = float(ah)
    br = float(ar)
except:
    print("Error, please enter numeric input")
    quit()

if bh > 40 :
    reg = bh * br
    otp = (bh - 40.0) * (br * 0.5)
    tp = reg + otp

else :
    tp = bh * br

print("Pay:",tp)
