def write_name(name):
    with open("student.txt",'a') as student:
        student.write(name + "\n")
    print("Saved Successfully!")

def read_name():
    try:
        with open("student.txt", 'r') as student:
            for name in student:
                print(f"Welcome Back {name.strip()}!")
    except FileNotFoundError:
        print("No student records found")

def main():
    name = input("Enter your name: ")
    write_name(name)
    read_name()

main()