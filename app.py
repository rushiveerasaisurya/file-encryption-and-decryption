import os
import sys
from flask import Flask, request, send_file, jsonify, render_template
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
import tempfile
import urllib.parse

app = Flask(__name__)

@app.route('/')
def index():
    """Serve the main page."""
    return render_template('index.html')

def generate_key(password: str, salt: bytes) -> bytes:
    """Generate a key from a password using PBKDF2HMAC."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    return key

def save_key(key: bytes, key_file: str):
    """Save the key to a file in base64 format."""
    with open(key_file, 'wb') as f:
        f.write(base64.b64encode(key))

def load_key(key_file: bytes) -> bytes:
    """Load the key from bytes."""
    return base64.b64decode(key_file)

@app.route('/encrypt', methods=['POST'])
def encrypt_file():
    """Encrypt a file using AES-256 in CBC mode."""
    if 'file' not in request.files or 'password' not in request.form:
        return jsonify({'error': 'Missing file or password'}), 400

    file = request.files['file']
    password = request.form['password']
    
    if not file or not password:
        return jsonify({'error': 'File or password cannot be empty'}), 400

    # Generate a random salt and IV
    salt = os.urandom(16)
    iv = os.urandom(16)
    
    # Generate key from password
    key = generate_key(password, salt)
    
    # Save key to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.key') as key_file:
        save_key(key, key_file.name)
        key_path = key_file.name.replace('\\', '/')  # Normalize to forward slashes

    # Read the input file
    data = file.read()
    
    # Pad the data to be a multiple of 16 bytes
    padding_length = 16 - (len(data) % 16)
    data += bytes([padding_length] * padding_length)
    
    # Encrypt the data
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(data) + encryptor.finalize()
    
    # Write encrypted data to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.encrypted') as enc_file:
        enc_file.write(salt + iv + encrypted_data)
        enc_path = enc_file.name.replace('\\', '/')  # Normalize to forward slashes

    return jsonify({
        'encrypted_file': enc_path,
        'key_file': key_path,
        'original_filename': file.filename
    })

@app.route('/decrypt', methods=['POST'])
def decrypt_file():
    """Decrypt a file using AES-256 in CBC mode."""
    if 'file' not in request.files or 'key' not in request.files:
        return jsonify({'error': 'Missing encrypted file or key file'}), 400

    file = request.files['file']
    key_file = request.files['key']
    
    if not file or not key_file:
        return jsonify({'error': 'Encrypted file or key file cannot be empty'}), 400

    # Load the key
    key = load_key(key_file.read())
    
    # Read the encrypted file
    data = file.read()
    
    # Extract salt, IV, and encrypted data
    salt = data[:16]
    iv = data[16:32]
    encrypted_data = data[32:]
    
    # Decrypt the data
    try:
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    except Exception as e:
        return jsonify({'error': f'Decryption failed: {str(e)}'}), 400
    
    # Remove padding
    padding_length = decrypted_data[-1]
    decrypted_data = decrypted_data[:-padding_length]
    
    # Write decrypted data to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.decrypted') as dec_file:
        dec_file.write(decrypted_data)
        dec_path = dec_file.name.replace('\\', '/')  # Normalize to forward slashes

    return jsonify({
        'decrypted_file': dec_path,
        'original_filename': file.filename.replace('.encrypted', '')
    })

@app.route('/download/<path:filename>')
def download_file(filename):
    """Serve a file for download."""
    try:
        # Decode URL-encoded filename and normalize path
        filename = urllib.parse.unquote(filename).replace('\\', '/')
        if not os.path.exists(filename):
            return jsonify({'error': 'File not found'}), 404
        return send_file(filename, as_attachment=True)
    except Exception as e:
        return jsonify({'error': f'Failed to serve file: {str(e)}'}), 500
    finally:
        # Clean up temporary file if it exists
        if os.path.exists(filename):
            try:
                os.remove(filename)
            except Exception as e:
                app.logger.error(f"Failed to delete temporary file {filename}: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
