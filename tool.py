import os
import json
import subprocess

def run_bash_cmd(command):
    """
    Runs a Bash command and prints its output/errors.
    """
    try:
        # Running bash command via -c flag
        process = subprocess.run(['bash', '-c', command], capture_output=True, text=True, check=True)
        return process.stdout
    except subprocess.CalledProcessError as e:
        # Print error if command execution fails
        print(f"Error executing command: {e.stderr if e.stderr else e}")
    except FileNotFoundError:
        # Error if bash binary is not found
        print("Error: Bash not found.")

def get_db_path():
    """
    Get the absolute path to the database file.
    """
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, 'db.json')

def main():
    """
    DESC: Main program run. Checks UFW status and enables it if inactive.
    ARGS: NONE
    RTNS: NONE
    """
    # Check if UFW is active using match-case
    match run_bash_cmd("sudo ufw status"):
        # If UFW is inactive, enable it and warn about default IP blocking
        case "Status: inactive\n":
            print("\nUFW currently disabled... ENABLING UFW\n\nREMINDER: All IPs blocked by default, add to whitelist to allow users to connect.\n")
            run_bash_cmd("sudo ufw enable")
        case "Status: active\n":
            # If UFW is active, continue with the program
            print("\nUFW enabled... continuing.\n")
    
    # Call the main program loop
    prgm()

def prgm():
    # Prompt user for what they want to do next
    start = input("ENTER CMD #:\n1) MANAGE Users (Add/Remove/Switch)\n2) SHOW Whitelist/Blacklist\n3) EXIT\n\n")
    match start:
        case '1':
            # Call user management function
            manager()
        case '2':
            # Show the whitelist and/or blacklist
            show_db()
        case '3':
            # Exit the application
            exit()

def manager():
    # Ask user specific details for modifying the lists
    name = input("\nUser Name? ")
    ip = input("User IP? ")
    
    # Protocol selection
    while True:
        protocol = input("Select protocol (tcp/udp/all): ").lower()
        if protocol in ['tcp', 'udp', 'all']:
            break
        print("Invalid protocol! Please enter 'tcp', 'udp', or 'all'")
    
    # Improved port input handling - one port at a time
    ports = []
    while True:
        ports_input = input("Enter a port number (or 'done' to finish, 'all' for all ports): ")
        
        if ports_input.lower() == 'all':
            ports = 'all'
            break
        elif ports_input.lower() == 'done':
            if not ports:
                print("Please enter at least one port or 'all'")
                continue
            break
            
        try:
            port = int(ports_input.strip())
            if 1 <= port <= 65535:
                if port not in ports:
                    ports.append(port)
                else:
                    print("Port already added!")
            else:
                print("Invalid port number! Ports must be between 1-65535")
        except ValueError:
            print("Invalid input! Please enter a number, 'done', or 'all'")

    w_b = input("Whitelist or Blacklist? (w/b) ")
    match w_b:
        case "w" | "b":
            pass
        case _:
            print("\nPlease specify white/black list!")
            manager()
            return

    db_file = get_db_path()
    if not os.path.exists(db_file):
        print(f"\nDatabase file '{db_file}' does not exist. Creating it now...\n")
        # Create the database file with initial structure
        with open(db_file, 'w') as file:
            json.dump({"whitelist": {}, "blacklist": {}}, file, indent=2)

    with open(db_file, 'r') as file:
        db = json.load(file)

    # Modified data structure to include ports and protocol
    user_data = {
        "ip": ip,
        "ports": ports,
        "protocol": protocol
    }

    match w_b:
        case 'w':
            match True:
                case _ if name in db.get("whitelist", {}) and db["whitelist"][name]["ip"] == ip:
                    print(f"\n{name} is already in the whitelist.\n")
                case _ if name in db.get("blacklist", {}) and db["blacklist"][name]["ip"] == ip:
                    switch = input(f"{name} is in the blacklist. Do you want to switch to whitelist? (y/n) ")
                    if switch == 'y':
                        db["blacklist"].pop(name)
                        db.setdefault("whitelist", {})[name] = user_data
                        # Generate UFW command for all ports at once
                        if ports == 'all':
                            if protocol == 'all':
                                run_bash_cmd(f"sudo ufw allow from {ip}")
                            else:
                                run_bash_cmd(f"sudo ufw allow from {ip} proto {protocol}")
                        else:
                            ports_str = ','.join(map(str, ports))
                            if protocol == 'all':
                                run_bash_cmd(f"sudo ufw allow from {ip} to any port {ports_str}")
                            else:
                                run_bash_cmd(f"sudo ufw allow from {ip} to any port {ports_str} proto {protocol}")
                        print(f"\n{name} has been moved to the whitelist.\n")
                case _:
                    db.setdefault("whitelist", {})[name] = user_data
                    # Generate UFW command for all ports at once
                    if ports == 'all':
                        if protocol == 'all':
                            run_bash_cmd(f"sudo ufw allow from {ip}")
                        else:
                            run_bash_cmd(f"sudo ufw allow from {ip} proto {protocol}")
                    else:
                        ports_str = ','.join(map(str, ports))
                        if protocol == 'all':
                            run_bash_cmd(f"sudo ufw allow from {ip} to any port {ports_str}")
                        else:
                            run_bash_cmd(f"sudo ufw allow from {ip} to any port {ports_str} proto {protocol}")
                    print(f"\n{name} has been added to the whitelist.\n")
        case 'b':
            match True:
                case _ if name in db.get("blacklist", {}) and db["blacklist"][name]["ip"] == ip:
                    print(f"\n{name} is already in the blacklist.\n")
                case _ if name in db.get("whitelist", {}) and db["whitelist"][name]["ip"] == ip:
                    switch = input(f"{name} is in the whitelist. Do you want to switch to blacklist? (y/n) ")
                    if switch == 'y':
                        db["whitelist"].pop(name)
                        db.setdefault("blacklist", {})[name] = user_data
                        # Generate UFW command for all ports at once
                        if ports == 'all':
                            if protocol == 'all':
                                run_bash_cmd(f"sudo ufw deny from {ip}")
                            else:
                                run_bash_cmd(f"sudo ufw deny from {ip} proto {protocol}")
                        else:
                            ports_str = ','.join(map(str, ports))
                            if protocol == 'all':
                                run_bash_cmd(f"sudo ufw deny from {ip} to any port {ports_str}")
                            else:
                                run_bash_cmd(f"sudo ufw deny from {ip} to any port {ports_str} proto {protocol}")
                        print(f"\n{name} has been moved to the blacklist.\n")
                case _:
                    db.setdefault("blacklist", {})[name] = user_data
                    # Generate UFW command for all ports at once
                    if ports == 'all':
                        if protocol == 'all':
                            run_bash_cmd(f"sudo ufw deny from {ip}")
                        else:
                            run_bash_cmd(f"sudo ufw deny from {ip} proto {protocol}")
                    else:
                        ports_str = ','.join(map(str, ports))
                        if protocol == 'all':
                            run_bash_cmd(f"sudo ufw deny from {ip} to any port {ports_str}")
                        else:
                            run_bash_cmd(f"sudo ufw deny from {ip} to any port {ports_str} proto {protocol}")
                    print(f"\n{name} has been added to the blacklist.\n")

    with open(db_file, 'w') as file:
        json.dump(db, file, indent=2)

    more = input("Do you want to add more users? (y/n) ")
    if more == 'y':
        manager()
    else:
        print("\nReturning to menu!\n")
        prgm()

def show_db():
    # Load database file if it exists, otherwise exit function
    db_file = get_db_path()
    if os.path.exists(db_file):
        with open(db_file, 'r') as file:
            db = json.load(file)
    else:
        print(f"\nDatabase file '{db_file}' not found.\n")
        return
    # Ask user which list to view: whitelist, blacklist or all
    which = input("\nWhich database would you like to see? Whitelist, Blacklist or All? (w/b/a)\n\n")
    # Selecting proper list to display using match-case
    match which:
        case "w":
            print("\n===== WHITELIST =====\n\n" + f"{json.dumps(db.get('whitelist', {}), indent=4)}\n")
        case "b":
            print("\n===== BLACKLIST =====\n\n" + f"{json.dumps(db.get('blacklist', {}), indent=4)}\n")
        case "a":
            print("\n===== ALL LISTS =====\n\n" + f"{json.dumps(db, indent=4)}\n")

# Starting the program
main()

# ------------------------------------------------------------------------------
# main structure:
# --- checking if UFW enabled ---
# If UFW is not enabled, it will be enabled automatically.
# Also displays a reminder that by default all IPs are blocked until added.
# Then moves into the main program loop: managing users, showing lists or exit.
#
# note:
# Feature ideas: SYNC current UFW rules, check whitelist against active rules,
# prompt for user names if mismatch occurs, and sync lists accordingly.
# ------------------------------------------------------------------------------