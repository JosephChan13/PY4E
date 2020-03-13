print("Conditional Statements - Exercise 1")

ah = input("Enter Hours: ")
ar = input("Enter Rate: ")
bh = float(ah)
br = float(ar)

if bh > 40 :
    reg = bh * br
    otp = (bh - 40.0) * (br * 0.5)
    tp = reg + otp

else :
    tp = bh * br

print("Pay:",tp)
