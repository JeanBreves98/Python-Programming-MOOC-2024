password = input("Password:")
while True:
    attempt = input("Repeat password:")
    if attempt != password:
        print("They do not match!")
    else:
        print("User account created!")
        break