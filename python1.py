port = int(input("Please enter port number to check its assigned service: "))

if port == 22:
    print("Port is for SSH")
elif port == 443:
    print("Port is for HTTPS")
elif port == 80:
    print("Port is for HTTP")
elif port == 3306:
    print("Port is for MYSQL")
else:
    print("Unknown port")

