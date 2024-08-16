# Ex9 - String
Text = "3 4 5 6"
# Q1 - Remove space and keep result = "3456"
result =""
for i in range(len(Text)):
    if Text[i] != " ":
        result += (Text[i])
print("result",result)


# Q2 - Multiple each letter by 2 result = "6 8 10 12"
result=""
for i in range(len(Text)):
    if Text[i] != " ":
        result += str(int(Text[i])*2)+" "
print("Multiple by 2: ",result)
