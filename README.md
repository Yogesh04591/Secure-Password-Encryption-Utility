# Secure-Password-Encryption-Utility
🔐 A Python-based password encryption and decryption utility using cryptography for secure database authentication and MySQL connection handling.

# 🔐 Password Encryption & Secure SQL Connection using Python

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Security](https://img.shields.io/badge/Security-Enabled-success?logo=lock)
![Encryption](https://img.shields.io/badge/Encryption-Fernet%20AES256-orange)
![Database](https://img.shields.io/badge/Database-MySQL-blue?logo=mysql)
![Status](https://img.shields.io/badge/Build-Passing-brightgreen)

A **secure Python project** that encrypts and decrypts passwords using the `cryptography.fernet` module — ensuring your credentials are **safe and never stored in plain text**.  
This project also demonstrates how to use **encrypted passwords** to establish **MySQL database connections securely**.

---

## 🧭 Table of Contents
- [✨ Overview](#-overview)
- [⚙️ Features](#️-features)
- [🧠 Concepts Used](#-concepts-used)
- [📁 Project Structure](#-project-structure)
- [💻 Installation & Setup](#-installation--setup)
- [🚀 How It Works](#-how-it-works)
- [🧩 Example Code](#-example-code)
- [🔒 Security Practices](#-security-practices)
- [🧱 Future Enhancements](#-future-enhancements)
- [📜 License](#-license)
- [👨‍💻 Author](#-author)

---

## ✨ Overview

Passwords stored in plain text are vulnerable to security breaches.  
This project eliminates that risk by:
- **Encrypting passwords** with a unique key generated using `Fernet`.
- **Decrypting** only when required (like during a MySQL connection).
- **Protecting credentials** even if your code or database is exposed.

🔹 Ideal for: Python developers, database admins, and anyone learning **data security**, **file handling**, or **modular programming**.

---

## ⚙️ Features

✅ Generates a **random encryption key** stored in a file (`secret_key.txt`)  
✅ Encrypts passwords **only once** and reuses them safely  
✅ Supports **decryption on demand** for real-time secure access  
✅ Uses **Fernet symmetric encryption** from the `cryptography` module  
✅ Securely connects to **MySQL databases** with encrypted credentials  
✅ Implements **clean modular design** for readability and reuse  

---

## 🧠 Concepts Used

| Concept | Description |
|----------|--------------|
| **Encryption & Decryption** | Protects data by converting it into unreadable format using `cryptography.fernet`. |
| **File Handling** | Stores and retrieves encryption keys securely. |
| **Modular Programming** | Divides logic into separate Python files (`password_utinels.py`, `encrypt_once.py`, etc.). |
| **Database Security** | Demonstrates how to connect to databases using encrypted credentials. |
| **Python Classes & Functions** | Encapsulates code for better reusability and clarity. |

---

## 💻 Installation & Setup

You can set up everything with just a few commands 👇  

```bash
# 1️⃣ Clone the repository
git clone https://github.com/yourusername/password-encryption-secure-sql.git
cd password-encryption-secure-sql

# 2️⃣ Create a virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate  # For Windows
# source venv/bin/activate  # For macOS/Linux

# 3️⃣ Install all dependencies
pip install cryptography pymysql

# 4️⃣ Run the encryption script to generate a key and encrypted password
python encrypt_once.py

# 5️⃣ Securely connect to your MySQL database
python connection_secure_sql.py

---

## 🧱 Future Enhancements

🧑‍💻 GUI for encryption/decryption
🔄 Automatic key rotation
☁️ Integration with AWS Secrets Manager
🧾 Logging and audit tracking

---

## 📜 License

This project is licensed under the MIT License.
You’re free to use and modify it with proper attribution.

---

## 👨‍💻 Author

Yogesh M
📧 Email: yogeshm04591@gmail.com
🌐 GitHub: https://github.com/Yogesh04591

“Security isn’t just a feature — it’s a mindset.” 🧠
