# Ex3 - String
# Enter text and check if it contains capital letter or not
text = input("Enter Text:")
found_text = False
message = ""
for i in range(len(text)):
    if text[i] == text[i].upper():
        found_text = True
if found_text:
    message  = "Yes"
else:
    message = "No"
print(message)