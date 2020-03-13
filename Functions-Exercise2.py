print("Functions - Exercise 2")

def computegrade(score):
    if score > 1.0:
        print("Bad Score")
        quit()
    elif score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    elif score < 0.0:
        print("Bad Score")
    elif score < 0.6:
        print("F")


    else:
        print("Bad Score")




rs = input("Enter Score: ")

try:
    rawscore = float(rs)

except:
    print("Bad Score")
    quit()

computegrade(rawscore)
