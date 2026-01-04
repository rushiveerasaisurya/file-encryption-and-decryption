# 🔐 File Encryption & Decryption (Flask)

Securely encrypt and decrypt files through a simple, responsive Flask web app. Upload any file, protect it with a password, and download the encrypted version and key for later decryption. [web:30][web:22]

---

## ✨ Features

- 🔑 Password-based AES-256 file encryption [web:38]
- 🧂 Secure key derivation using PBKDF2 (SHA-256 + salt) [web:38]
- 📁 File upload/download for encryption and decryption via Flask routes
- 🖥️ Clean HTML/CSS UI with separate sections for Encrypt & Decrypt
- 🧹 Temporary files used for encrypted/decrypted outputs

---

## 🗂️ Folder Structure

```bash
File-Encryption-and-Decryption--main/
├─ app.py                  # Flask backend (encryption & decryption logic)
├─ requirements.txt        # Python dependencies
├─ README.md               # Project documentation
└─ templates/
   └─ index.html           # Frontend HTML (UI for encrypt/decrypt)
