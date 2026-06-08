#loops and things

port_open = False
attempts = 0

while not port_open and attempts < 5:
    print(f"Checking port... Attempts {attempts + 1}")

    if attempts == 3:
        port_open = True
    attempts += 1
print("port is open")

# search services
services = ["nginx", "postgres", "redis"]
service = input("enter service name ")
for serviced in services:
    print(f"checking {service}")
    if serviced == service:
        print("found it")
        break
    else:
        print("service not in list")
    
try:
    age = int(input("Your age: "))
    print(f"You are {age} year old")

except ValueError:
    print("error: please enter a number")

