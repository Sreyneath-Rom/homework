# Ex8 - String
text = "9394884039"
# Q1 - How many number 8 in string
count_number8= 0
for i in range(len(text)):
    if text[i] == "8":
        count_number8 += 1
print("number 8 in string:",count_number8)
# Q2 - What is first index of letter 8
found = False
for i in range(len(text)):
    if text[i] == "8" and not found:
        found = True
        print("First index of 8: ", i)



