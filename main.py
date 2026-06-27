import re
import platform
import socket

def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score == 5:
        return "Very Strong Password 🔐"
    elif score >= 3:
        return "Medium Password ⚠️"
    else:
        return "Weak Password ❌"


def show_system_info():
    print("\n--- System Info ---")
    print("OS:", platform.system())
    print("Version:", platform.version())
    print("Machine:", platform.machine())


def show_ip():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    print("\n--- Network Info ---")
    print("Hostname:", hostname)
    print("IP Address:", ip)


if __name__ == "__main__":
    print("=== Cybersecurity Learning Tool ===")

    while True:
        print("\n1. Check Password Strength")
        print("2. Show System Info")
        print("3. Show IP Info")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            pw = input("Enter password: ")
            print(check_password_strength(pw))

        elif choice == "2":
            show_system_info()

        elif choice == "3":
            show_ip()

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")
