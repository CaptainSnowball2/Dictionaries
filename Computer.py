People={"Bob":"Welcom2022","Levi":"Chicken1290","Arno":"Qwerty1209Arnoisverycool123409","Anjali":"A123IqwertyArnoqwertyqwertyqwertyqwerty"}
A=input("Username: ")
if A in People:
    B=input("Password: ")
    if B==People[A]:
        print("Logged In Successfully")
    else:
        print("incorrect Password")
else:
    print("Incorrect Username")

