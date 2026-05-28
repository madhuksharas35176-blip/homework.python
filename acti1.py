age = input("Enter your age: ")

if age.isdigit():
    age = int(age)

    if age % 2 == 0:
        print("Age is Even")
    else:
        print("Age is Odd")

else:
    print("Value Error! Please enter only integer values.")