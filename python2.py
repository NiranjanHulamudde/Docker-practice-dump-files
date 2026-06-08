infrastructure = {
        "web": {
            "name": "web1",
            "ip": "192.62.12.3",
            "port": 8080
        },
        "db": {
            "name": "db1",
            "ip": "192.168.1.4",
            "port": 5432
        }
}

print(infrastructure["web"]["name"])
print(infrastructure["db"]["port"])


for service, details in infrastructure.items():
    print(f"{service}: {details['name']}")

# new lesson


age = int(input("please type your age: "))

if age >= 25:
    print("you are an adult")
else:
    print("you are not an adult")


container = "running"
cpu = int(input("type cpu usage "))
memory = int(input("type memory usage "))

if container == "running":
    print("container is running")

if cpu > 85 or memory > 85:
    print("memory or cpu is high")
elif cpu > 60 or memory > 60:
    print("resourse use is moderate")
else:
    print("resourse is normal")


allow_ports = [8080, 443, 3306, 5432]
port = int(input("type port number "))

if port in allow_ports:
    print(f"port {port} is allowed")
else:
    print(f"port {port} is not allowed")


#practice


allowed_ports = [8080, 443, 3306, 5432]
ports_check = [8080, 9000, 443, 2222]

for port in ports_check:
    if port in allowed_ports:
        print(f"port {port} is allowed")
    else:
        print(f"port {port} is blocked")

#restarting services

services = ["nginx", "postgres", "redis", "mongo"]

for service in services:
    print(f"Restarting {service}...")
    if service == "postgres":
        print("PostgreSQL restarted successfully")
        break


# skip unhealthy checks

service_health = {
        "nginx": "healthy",
        "postgres": "unhealthy",
        "redis": "healhty",
        "mongo": "unhealthy"
        }

for service, health in service_health.items():
    if health == "unhealthy":
        continue
    print(f"{service} is {health} - monitoring active")




# for loops and control flow

