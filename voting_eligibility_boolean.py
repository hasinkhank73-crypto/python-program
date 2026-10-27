
age = int(input("Enter your age: "))
permission = input("Do you have special voting permission? (yes/no): ")

if age >= 18 or permission == "yes":
    print("Person is eligible to vote.")
else:
    print("Person is not eligible to vote.")
