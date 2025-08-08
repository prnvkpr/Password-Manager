# 🔐 Python Password Manager

A lightweight command-line password manager built with **Python**, **Fernet encryption**, and **clipboard integration** for quick password access.  
It allows you to **securely store, view, delete, search, and generate passwords** — all encrypted with your **master password**.

---

## 🚀 Features

- **Secure Storage** — Passwords are encrypted with [cryptography.fernet](https://cryptography.io/en/latest/fernet/).
- **Master Password Protection** — Access is gated by a master password.
- **Clipboard Copying** — Passwords are automatically copied to your clipboard (via `pyperclip`).
- **Search Functionality** — Quickly find stored accounts.
- **Random Password Generator** — Creates strong passwords with letters, numbers, and symbols.
- **Delete Feature** — Remove any account’s credentials from storage.
- **Cross-platform** — Works on Windows, macOS, and Linux.

---

## 📦 Requirements

Make sure you have Python **3.7+** installed.  
Install the required dependencies:

```bash
pip install cryptography pyperclip
```

## ⚙️ Setup
Clone this repository
```
git clone https://github.com/yourusername/password-manager.git
cd password-manager
```
Generate your encryption key (only once)
```
from cryptography.fernet import Fernet
with open("key.key", "wb") as key_file:
    key_file.write(Fernet.generate_key())
```
Run the password manager
```
python main.py
```

## 🖥️ Usage
Once you start the program, enter your master password (currently hardcoded as prnv in main() — you can change this for security).

Available commands:
| Command    | Description                                      |
| ---------- | ------------------------------------------------ |
| `add`      | Add a new account and password                   |
| `view`     | View all stored accounts and retrieve a password |
| `delete`   | Delete an account’s stored credentials           |
| `search`   | Search for an account’s credentials              |
| `generate` | Generate a secure random password and store it   |
| `q`        | Quit the program                                 |

## 🔐 Security Notes
All passwords are encrypted using Fernet symmetric encryption before being saved to password.txt.

Your key.key and password.txt files must be kept safe.
If someone gains access to both and your master password, they can decrypt your passwords.

Do not commit key.key or password.txt to version control (add them to .gitignore).

## 📄 File Structure
```
password-manager/
│
├── main.py           # Main script
├── key.key           # Encryption key file (generated once)
├── password.txt      # Encrypted password storage
└── README.md         # Project documentation
```

## 📜 License
This project is licensed under the MIT License — feel free to use, modify, and distribute.
