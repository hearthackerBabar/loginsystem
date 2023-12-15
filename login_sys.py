# ASCII art for "Welcome Back"
welcome_back_art = r"""

 __      _____ _    ___ ___  __  __ ___  
 \ \    / / __| |  / __/ _ \|  \/  | __| 
  \ \/\/ /| _|| |_| (_| (_) | |\/| | _|  
   \_/\_/ |___|____\___\___/|_|  |_|___| 
                                         
"""

print(welcome_back_art)

# Key for authentication
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def login():
    stored_key = "MRrEBM9JTU3zJ7i35zxp"
    entered_key = input("Enter the key: ")

    if entered_key == stored_key:
        clear_screen()
        print("Login successful!")
        time.sleep(2)
        clear_screen()
        display_options()
        select_option()
    else:
        clear_screen()
        print("Invalid key")

def display_options():
    print("Select an option:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Option 4")
    print("5. Option 5")

def select_option():
    option = input("Select an option (1-5): ")
    clear_screen()
    if option.isdigit() and 1 <= int(option) <= 5:
        print(f"You selected option {option}")
    else:
        print("Invalid option")

# Test the login function
login()
