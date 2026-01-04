# File Encryption & Decryption Web Application

A secure web application for encrypting and decrypting files using AES-256 in CBC mode. Built with a Flask backend and a responsive HTML/CSS frontend, this project allows users to upload files, encrypt them with a password, and decrypt them using a key file. The interface uses Flexbox with `justify-content: space-around` for a clean, evenly spaced layout.

## Features
- **Encryption**: Encrypt any file (e.g., text, images) using AES-256 in CBC mode with a user-provided password.
- **Decryption**: Decrypt files using the corresponding key file generated during encryption.
- **Secure Key Management**: Generates and saves encryption keys securely using PBKDF2HMAC for key derivation.
- **Responsive Frontend**: Built with HTML, JavaScript, and plain CSS, using Flexbox for layout with `space-around` for even spacing of form elements.
- **Temporary File Handling**: Files are stored temporarily on the server and deleted after download to ensure security.

## Technologies Used
- **Backend**: Python, Flask, `cryptography` library
- **Frontend**: HTML, JavaScript, CSS (Flexbox with `space-around`)
- **Encryption**: AES-256 in CBC mode with PBKDF2HMAC for key derivation

## Prerequisites
- Python 3.6+
- Git
- A web browser (e.g., Chrome, Firefox)

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>


Install Dependencies:
pip install flask cryptography


Project Structure:Ensure the following structure:
<your-repo-name>/
├── app.py
├── templates/
│   └── index.html
├── document.txt (optional, for testing)


Run the Application:
python app.py


The server will start at http://127.0.0.1:5000.
Open this URL in a browser to access the web interface.



Usage

Encrypt a File:

Navigate to http://127.0.0.1:5000.
In the "Encrypt a File" section, upload a file (e.g., document.txt) and enter a password.
Click "Encrypt" to generate and download an encrypted file (.encrypted) and a key file (.key).


Decrypt a File:

In the "Decrypt a File" section, upload the encrypted file and its corresponding key file.
Click "Decrypt" to download the original file.


Test with Sample File:

Use the provided document.txt or create your own file to test encryption/decryption.
Example document.txt content:This is a sample document for testing the file encryption and decryption project.
It contains multiple lines of text.
You can use this file to test the encryption and decryption functionality.
Feel free to modify the content as needed!





Security Notes

Key Storage: The key file (.key) is required for decryption. Store it securely, as it cannot be recovered if lost.
Password: The encryption password is used to derive the key using PBKDF2HMAC. Use a strong password.
Temporary Files: Files are deleted after download to prevent unauthorized access.
Production: For production, deploy with HTTPS using a WSGI server (e.g., Gunicorn) to secure file uploads.

Deployment to GitHub
To deploy the project to GitHub:

Create a Repository:

Go to GitHub, sign in, and create a new repository (e.g., file-encryption-web).
Initialize it with a README (optional, as it will be overwritten).


Push the Code:
git init
git add app.py templates/index.html document.txt
git commit -m "Initial commit: File encryption and decryption web app"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo-name>.git
git push -u origin main









Creating requirements.txt
pip freeze > requirements.txt

Example requirements.txt:
Flask==2.0.1
cryptography==38.0.1

Example Screenshots

Home Page: Displays encryption and decryption forms with evenly spaced elements using Flexbox space-around.
Encryption: Upload a file, enter a password, and download encrypted/key files.
Decryption: Upload encrypted and key files to retrieve the original file.

Troubleshooting

404 Error: Ensure index.html is in the templates folder and app.py has a / route.
500 Error: Check the terminal for tracebacks. Common issues include file path errors or missing dependencies.
File Downloads: If downloads fail, verify temporary file paths and permissions in app.py.

Contributing
Contributions are welcome! Fork the repository, make changes, and submit a pull request.
License
This project is licensed under the MIT License.
Contact
For issues or suggestions, open an issue on GitHub or contact .```
