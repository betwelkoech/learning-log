
secret = "Jambazi"
max_tries = 3
for attempt in range(1, max_tries+1):
    guess = input("Enter the password: ")
    if secret==guess:
       print("Access granted")
       break
    print(f"Access denied. Attempt {attempt} of {max_tries}")
else:
    print("Too many failed attempts. Exiting.")
