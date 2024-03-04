def welcome_user(name, age):
    print("Hello,", name, "!")

    if age >= 18:
        print("You are an adult.")
    else:
        print("You are not an adult.")

if __name__ == "__main__":
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    welcome_user(name, age)
