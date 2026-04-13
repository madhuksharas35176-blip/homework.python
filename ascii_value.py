ch = input("Enter a character: ")

if len(ch) != 1:
    print("Error: Please enter only one character")
else:
    ascii_value = ord(ch)
    print("ASCII value:", ascii_value)

    if ch.isupper():
        print("Type: Uppercase Letter")
    elif ch.islower():
        print("Type: Lowercase Letter")
    elif ch.isdigit():
        print("Type: Digit")
    else:
        print("Type: Special Character")