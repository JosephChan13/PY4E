print("Functions - Exercise 1")

def computepay(hours, rate) :
    if hours > 40 :
        reg = hours * rate
        otp = (hours - 40.0) * (rate * 0.5)
        pay = reg + otp
    else :
        pay = hours * rate
    return pay

ah = input("Enter Hours: ")
ar = input("Enter Rate: ")
bh = float(ah)
br = float(ar)

tp = computepay(bh,br)

print("Pay:",tp)
