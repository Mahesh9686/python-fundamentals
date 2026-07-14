def menu():

    print("=" * 40)
    print("EMPLOYEE MANAGEMENT SYSTEM")
    print("=" * 40)

    print("1. Add Employee")
    print("2. Exit")
    try:
        option = int(input("Select option: "))
        return option
    except ValueError:
        print("Enter numbers only!")
        return None


def main():

    while True:

        selection = menu()

        if selection == 1:
            print("Adding Employee...")

        elif selection == 2:
            print("Good Bye")
            break

        else:
            print("Please Enter Valid option")
            continue


main()