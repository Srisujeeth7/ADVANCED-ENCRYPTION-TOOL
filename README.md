# ADVANCED-ENCRYPTION-TOOL

COMPANY: CODTECH IT SOLUTIONS

NAME: SRI SUJEETH SIRIVELLA

INTERN ID: CT04DN1954

DOMAIN: CYBER SECUTITY & ETHICAL HACKING.

DURATION: 4 WEEEKS

MENTOR: NEELA SANTOSH

TASK DESCRIPTION : ADVANCED ENCRYPTION TOOL

# Project Description.

In the digital age, securing sensitive data has become an absolute necessity. Whether it's personal information, financial records, or classified business files, protecting digital assets from unauthorized access is crucial. This project aims to develop a robust Advanced Encryption Tool that leverages AES-256 encryption — one of the most secure and widely used encryption algorithms in the world. The objective is to create a user-friendly Python application that enables users to encrypt and decrypt files using strong password-based security, ensuring confidentiality and integrity.

## Objective
The main goal of this task is to create a secure, reliable, and easy-to-use application that:

Allows users to encrypt files with AES-256-bit encryption.

Allows decryption of previously encrypted files using the correct password.

Provides a GUI (Graphical User Interface) to make the tool accessible to non-technical users.

Ensures that no sensitive data (like passwords) is stored insecurely or logged during usage.

🔧 Tools & Technologies Used
Programming Language: Python

Encryption Library: cryptography (uses PBKDF2, Fernet, AES under the hood)

Key Derivation Function: PBKDF2HMAC with SHA256 for converting passwords into secure keys

GUI Framework: tkinter for building the interface

File Handling: Standard Python I/O methods

## Encryption Methodology.

The tool uses AES-256 (Advanced Encryption Standard with 256-bit keys), which is a symmetric encryption algorithm. AES-256 is considered military-grade encryption and is trusted by governments and security agencies worldwide. Since AES is symmetric, it requires the same key for both encryption and decryption.

To convert a human-readable password into a 256-bit AES key, the system uses PBKDF2 (Password-Based Key Derivation Function 2) along with a random salt. This process ensures that even if two users input the same password, the resulting keys will differ due to the unique salt, making it highly resistant to dictionary and rainbow table attacks.

The Fernet module, provided by the cryptography library, is used as a high-level wrapper that manages AES encryption/decryption along with signing (for integrity). It automatically handles padding, IV (Initialization Vector) generation, and base64 encoding of the final encrypted content.

## GUI Functionality.

The application uses tkinter to build a lightweight graphical interface. The GUI allows users to:

Browse and select a file from their system.

Enter a password for encryption or decryption.

Click a button to either encrypt or decrypt the selected file.

Receive success/failure notifications through popup messages.

This makes the tool suitable for users with minimal technical expertise.

## Security Features.

Each encryption operation uses a unique salt to derive the key, making brute-force attempts extremely difficult.

No passwords are stored; all encryption keys are generated on-the-fly and discarded after use.

The .aes extension is appended to encrypted files to distinguish them.

Any tampering with the encrypted file will lead to a decryption failure, preserving data integrity.

## Use Cases.

Encrypting sensitive documents (e.g., resumes, IDs, research papers)

Securely storing backup files

Sending confidential files over insecure networks

Personal or academic data protection

## Learning Outcomes.

This project provides hands-on experience in:

Working with modern cryptographic libraries in Python

Building real-world GUI applications

Understanding key concepts like AES, symmetric encryption, password-based key derivation

Implementing security best practices (e.g., using salts, securing password entry)

## Conclusion.
The Advanced Encryption Tool is a powerful demonstration of how strong cryptographic practices can be combined with user-friendly design to create secure software. By using AES-256 encryption and Python’s cryptography library, this tool offers a practical solution for file protection that balances technical strength with usability. It serves as an excellent foundation for future enhancements such as folder encryption, drag-and-drop support, or even web-based encryption services.

