
# Ex5 - String 
Text = "454639"
# Q1 - Count odd and even number in Text
count_odd = 0
count_even = 0
for number in Text:
    if int(number) % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print("Even count:", count_even)
print("Odd count:", count_odd)

# Q2 - Sum all number
sum = 0
for number in Text:
    sum += int(number)
print("Sum of all numbers:", sum)

# Q3 - Sum only even numbers
sum = 0
for number in Text:
    if int(number) % 2 == 0:
        sum += int(number)
print("sum only even number:",sum)

# Q4 - Reverse
reversed = len(Text)-1
result=""
for i in range(len(Text)):
    result += Text[reversed-i]
print("reversed text:",result)



