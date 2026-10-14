names = []

for i in range(3):
    name = input("Enter a name: ").strip()
    names.append(name)   # add the name to the list
    
print("Alphabetical order:")
for name in sorted(names, key=str.lower):  # sort names ignoring case
    print(name) 
print("Reverse alphabetical order:")
for name in sorted(names, reverse=True, key=str.lower):
    print(name)