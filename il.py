def shutdown():
    choice = input("Enter Yes or No: ")

    if choice == "Yes":
        print("Shutting down")
    elif choice == "No":
        print("Abort shutdown")
    else:
        print("Sorry")

shutdown()