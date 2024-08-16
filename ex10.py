# Ex10 - Number
# Enter 5 numbers and find maximum and minimum value
# Example:
# 1
# 5
# 6
# 7
# 0
# output : Max = 7, Min = 0


max = None
min = None
for i in range(5):
    number = int(input("Enter number: "))  
    if max is None and min is None:
        max = number
        min = number
    else:
        if number > max:
            max = number
        if number < min:
            min = number
print("Max =", max)
print("Min =", min)

    
