# Ex7 - number
# Enter number in range 10 - 20 until you enter other number out of range
# display "Continue" if number in range 10 - 20
# display "Out of range" if number difference from range 10 - 20

number = int(input("Enter a number in the range 10 - 20: ")) 
if number <=10 or number <= 20:
    print("Continue")
else:
    print("Out of range")

