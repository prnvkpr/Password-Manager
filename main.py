from cryptography.fernet import Fernet 
from tkinter import *
import pyperclip
import random
import string

# window = Tk()
# window.geometry("500x500")
# window.title("password manager")
# window.config(background="black")
# window.mainloop()

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key
master_password = input("Enter Master Password \n")

key = load_key() + master_password.encode()
f = Fernet(key)

def view() :
    global user 
    global passw
    with open("password.txt", "r") as file :
        for line in file.readlines() :
            clean_line = line.rstrip()
            user, passw = clean_line.split("|")
            print(f"User : {user}")
    choice = input("which password would you like to see? \n")
    with open("password.txt", "r") as file :
        lines = file.readlines()
        if not lines :
            print("nothing found")
        else :
            for line in lines:
                clean_line = line.rstrip()
                if choice in line :
                    user, passw = clean_line.split("|")
                    encrypted_pass = f.decrypt(passw.encode()).decode()
                    pyperclip.copy(encrypted_pass)
                    print(f"User : {user} | Password : {pyperclip.paste()}")
                else : 
                    pass


def add() :
    global account
    account = input("Enter Account Name")
    passw = input("Enter Password")
    encrypted_pass = f.encrypt(passw.encode()).decode()
    with open("password.txt", "a") as file :
        file.write(f"{account} | {encrypted_pass} \n")

def delete(): 
    with open("password.txt", "r") as file :
        for line in file.readlines():
            clean_line = line.rstrip()
            user, passw = clean_line.split("|")
            print(user)
        account_choosed = input("What password would you like to delete? \n")
        with open("password.txt", "r") as file : 
            for line in file.readlines():
                if account_choosed in line :
                    new_lines = []
                    with open("password.txt", "r") as file :
                        for line in file.readlines() :
                            if account_choosed not in line :
                                new_lines.append(line)
                    with open("password.txt", "w") as file :
                        file.writelines(new_lines)

def search() :
    search_ = input("Enter the account you want to search \n")
    with open("password.txt", "r") as file :
        for line in file.readlines() :
            clean_line = line.rstrip()
            if search_ in line :
                user, passw = clean_line.split("|")
                encrypted_pass = f.decrypt(passw.encode()).decode()
                pyperclip.copy(encrypted_pass)
                print(f"User : {user} | Password : {pyperclip.paste()}")

def generate(length=9) :
    account_name = input("Enter the Account Name")
    character = string.ascii_letters + string.punctuation + string.digits
    password = "".join(random.choice(character) for i in range(length))
    with open("password.txt", "w") as file :
        file.write(f"{account_name} | {password} \n")
    with open("password.txt", "r") as file : 
        for line in file.readlines():
            clean_line = line.rstrip()
            if account_name in line :
                user, passw = clean_line.split("|")
                encrypted_pass = f.encrypt(password.encode()).decode()
                pyperclip.copy(encrypted_pass)
                print(f"User : {user} | Password : {pyperclip.paste()}")





def main() :
    if master_password == "prnv" :
        while True :
            response = input("Would you like to (add), (view), (delete), (search) or generate a password? Type q to quit \n")
            if response.lower() == "add" :
                add()
            elif response.lower() == "view" :
                view()
            elif response.lower() == "delete" :
                delete()
            elif response.lower() == "search" :
                search()
            elif response.lower() == "generate" :
                generate()
            else :
                quit()

if __name__ == "__main__" :
    main()
            