import json
import sys

def load_config(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"ERROR: {filename} not found")
        return None
    except json.JSONDecodeError:
        print("ERROR: Invalid JSON format")
        return None

def save_config(filename, config):
    try:
        with open(filename, "w") as file:
            json.dump(config, file, indent=2)
        print(f"Config save to {filename}")
    except Exception as e:
        print(f"ERROR: could not save config - {e}")

def list_services(config):
    print("\n--- Available Services ---")
    for service, details in config["services"].items():
        status = details.get("status", "unknown")
        image = details.get("image", "unknown")
        print(f"{service}: {image} ({status})")


def get_service_info(config, service_name):
    if service_name not in config["services"]:
        print(f"ERROR: Service '{service_name}' not found")
        return None
    return config["services"][service_name]

def change_status(config, service_name, new_status):
    if service_name not in config["services"]:
        print(f"ERROR: Service '{service_name}' not found")
        return False

    valid_statuses = ["running", "stopped", "error"]
    if new_status not in valid_statuses:
        print(f"ERROR: Status must be one of {valid_statuses}")
        return False

    config["services"][service_name]["status"] = new_status
    print(f"Service '{service_name}' status changed to '{new_status}'")
    return True

def main():
    config_file = "docker-config.json"
    config = load_config(config_file)

    if config is None:
        return

    while True:
        print("\n--- Docker Config Manager ---")
        print("1. List services")
        print("2. Get service info")
        print("3. Change service status")
        print("4. Save and exit")

        choice = input("\nEnter choice (1-4): ")

        if choice == "1":
            list_services(config)

        elif choice == "2":
            service = input("Enter service name: ")
            info = get_service_info(config, service)
            if info:
                print(f"\nService: {service}")
                for key, value in info.items():
                    print(f" {key}: {value}")


        elif choice == "3":
            service = input("Enter service name: ")
            new_status = input("Enter new status (running/stopped/error): ")
            change_status(config, service, new_status)

        elif choice == "4":
            save_config(config_file, config)
            print("Goodbye!")
            break

        else:
            print("Invalid choice")

def main():
    config_file = "docker-config.json"
    config = load_config(config_file)

    if config is None:
        return

    print(f"Debug: config = {config}")
    print(f"Debug: services = {config.get('service', 'Not found')}")


if __name__ == "__main__":
    main()

