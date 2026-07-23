# 🔐 CipherForge

### Educational Cryptography Toolkit

<p align="center">
  <b>Explore. Encrypt. Decrypt. Analyze.</b>
</p>

<p align="center">
  A modular Python-based toolkit for exploring classical cryptography, encryption, decryption, and basic cipher analysis.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Version](https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</p>

---

## 📌 Overview

**CipherForge** is an educational cryptography toolkit developed as part of **DecodeLabs Cybersecurity Project 2**.

The project demonstrates the fundamental principles of:

* Encryption
* Decryption
* Plaintext and ciphertext
* Key-based transformations
* Classical cryptography
* Brute-force analysis
* Input validation
* Modular Python architecture

CipherForge provides an interactive command-line interface for experimenting with classical cryptographic algorithms.

The current implementation includes:

* **Caesar Cipher**
* **Vigenère Cipher**
* **Caesar Brute-Force Analysis**

---

## 🎯 Project Objectives

CipherForge was developed to:

* Understand how encryption transforms plaintext into ciphertext.
* Understand how decryption reverses an encryption process.
* Implement classical cryptographic algorithms using Python.
* Work with numerical and alphabetic encryption keys.
* Demonstrate the weaknesses of simple cryptographic algorithms.
* Implement brute-force analysis against a limited keyspace.
* Practice modular software architecture.
* Implement input validation and error handling.
* Build a practical educational cybersecurity project.

---

## ✨ Features

### 🔒 Caesar Cipher

The Caesar Cipher encrypts and decrypts text using a configurable numerical shift key.

#### Example

```text
╔══════════════════════════════════════════════════════════╗
║                    CAESAR CIPHER                        ║
╚══════════════════════════════════════════════════════════╝

Enter text: Muhammad Zubair
Enter shift key: 3

───────────────────────────────────────────────────────
Original Text  : Muhammad Zubair
Encrypted Text : Pxkdppdg Cxedlu
Decrypted Text : Muhammad Zubair
───────────────────────────────────────────────────────
```

The implementation:

* Preserves uppercase characters.
* Preserves lowercase characters.
* Preserves spaces.
* Preserves numbers and special characters.
* Supports custom numerical shift values.
* Uses modular arithmetic for alphabet wrapping.

For example:

```text
A + 3 = D
B + 3 = E
Z + 3 = C
```

---

### 🔐 Vigenère Cipher

The Vigenère Cipher uses an alphabetic key to apply changing shifts throughout the message.

#### Example

```text
╔══════════════════════════════════════════════════════════╗
║                   VIGENÈRE CIPHER                       ║
╚══════════════════════════════════════════════════════════╝

Enter text: M
Enter key: E

───────────────────────────────────────────────────────
Original Text  : M
Encrypted Text : Q
Decrypted Text : M
───────────────────────────────────────────────────────
```

The Vigenère Cipher requires an alphabetic key.

For example:

```text
Valid Key:
LEMON
SECRET
E
```

Invalid keys such as:

```text
3
123
KEY123
```

are rejected by the application.

Example validation response:

```text
[!] Error: Key must contain alphabetic characters only.
```

This demonstrates basic input validation before performing a cryptographic operation.

---

### 🔍 Caesar Brute-Force Analysis

CipherForge can attempt all **26 possible Caesar Cipher shifts**.

#### Example

```text
╔══════════════════════════════════════════════════════════╗
║              CAESAR BRUTE-FORCE ANALYSIS                 ║
╚══════════════════════════════════════════════════════════╝

Enter ciphertext: pxkdppdg Cxedlu

Possible decryptions:

Shift  0 │ pxkdppdg Cxedlu
Shift  1 │ owjcoocf Bwdckt
Shift  2 │ nvibnnbe Avcbjs
Shift  3 │ muhammad Zubair
Shift  4 │ ltgzllzc Ytazhq
Shift  5 │ ksfykkyb Xszygp
...
```

The correct plaintext appears at:

```text
Shift 3 │ muhammad Zubair
```

This demonstrates why the Caesar Cipher is vulnerable to brute-force attacks.

Since the Caesar Cipher has only 26 possible shifts, an attacker can test the entire keyspace quickly.

---

## 🖥️ Interactive Command-Line Interface

CipherForge provides a menu-driven terminal interface:

```text
╔══════════════════════════════════════════════════════════╗
║                    CIPHERFORGE MENU                     ║
╠══════════════════════════════════════════════════════════╣
║  [1] Caesar Cipher                                      ║
║  [2] Vigenère Cipher                                    ║
║  [3] Caesar Brute-Force Analysis                        ║
║  [4] About CipherForge                                  ║
║  [5] Help                                               ║
║  [0] Exit                                               ║
╚══════════════════════════════════════════════════════════╝
```

Available options:

| Option | Function                                  |
| ------ | ----------------------------------------- |
| `1`    | Caesar Cipher encryption and decryption   |
| `2`    | Vigenère Cipher encryption and decryption |
| `3`    | Caesar brute-force analysis               |
| `4`    | Project information                       |
| `5`    | Help and usage information                |
| `0`    | Exit the application                      |

---

## 🎨 CipherForge Interface

When launched, the application displays the CipherForge identity banner:

```text
 ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗ ███████╗ ██████╗ ██████╗  ██████╗ ███████╗
██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗██╔════╝██╔═══██╗██╔══██╗██╔════╝ ██╔════╝
██║     ██║██████╔╝███████║█████╗  ██████╔╝█████╗  ██║   ██║██████╔╝██║  ███╗█████╗
██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗██╔══╝  ██║   ██║██╔══██╗██║   ██║██╔══╝
╚██████╗██║██║     ██║  ██║███████╗██║  ██║███████╗╚██████╔╝██║  ██║╚██████╔╝███████╗
 ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝

        Educational Cryptography Toolkit
        Version 1.0.0
        Developed by Muhammad Zubair
```

The interface is designed to provide a clear, structured terminal experience while keeping the project focused on the underlying cryptographic concepts.

---

## 🧠 Supported Algorithms

| Algorithm          | Type                  | Status        |
| ------------------ | --------------------- | ------------- |
| Caesar Cipher      | Substitution Cipher   | ✅ Implemented |
| Vigenère Cipher    | Polyalphabetic Cipher | ✅ Implemented |
| Caesar Brute-Force | Cipher Analysis       | ✅ Implemented |
| Frequency Analysis | Cryptanalysis         | 🔜 Planned    |
| File Encryption    | Educational Feature   | 🔜 Planned    |

---

## 🏗️ Application Architecture

```text
                         ┌─────────────────────┐
                         │       User          │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │    CLI Interface    │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │  Input Validation   │
                         └──────────┬──────────┘
                                    │
                    ┌───────────────┼───────────────┐
                    │               │               │
                    ▼               ▼               ▼
             ┌────────────┐ ┌────────────┐ ┌───────────────┐
             │   Caesar   │ │ Vigenère   │ │   Brute-Force │
             │   Cipher   │ │   Cipher   │ │    Analysis   │
             └─────┬──────┘ └─────┬──────┘ └───────┬───────┘
                   │              │                │
                   └──────────────┼────────────────┘
                                  │
                                  ▼
                         ┌─────────────────────┐
                         │   Cipher Output     │
                         └─────────────────────┘
```

---

## 📂 Project Structure

```text
CipherForge/
│
├── cipherforge/
│   ├── __init__.py
│   ├── banner.py
│   ├── caesar.py
│   ├── vigenere.py
│   ├── cli.py
│   └── utils.py
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

### Module Description

| File               | Purpose                                                 |
| ------------------ | ------------------------------------------------------- |
| `main.py`          | Application entry point                                 |
| `__init__.py`      | Package metadata and version information                |
| `banner.py`        | CipherForge ASCII banner and identity                   |
| `caesar.py`        | Caesar encryption, decryption, and brute-force analysis |
| `vigenere.py`      | Vigenère encryption and decryption                      |
| `cli.py`           | Interactive command-line interface                      |
| `utils.py`         | Input validation and utility functions                  |
| `requirements.txt` | Project dependency list                                 |
| `.gitignore`       | Files excluded from Git tracking                        |
| `LICENSE`          | Project license                                         |

---

## 🚀 Installation

### Prerequisites

* Python 3.10 or newer
* Git
* A terminal or command prompt

### Clone the Repository

```bash
git clone https://github.com/phantomroot0x/CipherForge.git
```

### Navigate to the Project

```bash
cd CipherForge
```

### Run CipherForge

```bash
python main.py
```

---

## 💻 Usage

After launching:

```bash
python main.py
```

The CipherForge banner and main menu will be displayed.

Select an operation by entering its corresponding number.

### Caesar Cipher

```text
[1]
```

Enter:

```text
Text: Muhammad Zubair
Shift Key: 3
```

The application displays:

```text
Original Text  : Muhammad Zubair
Encrypted Text : Pxkdppdg Cxedlu
Decrypted Text : Muhammad Zubair
```

### Vigenère Cipher

```text
[2]
```

Enter an alphabetic key:

```text
Text: M
Key: E
```

The application displays:

```text
Original Text  : M
Encrypted Text : Q
Decrypted Text : M
```

### Caesar Brute-Force Analysis

```text
[3]
```

Enter ciphertext:

```text
pxkdppdg Cxedlu
```

CipherForge generates all 26 possible Caesar shifts and displays the results.

---

## 🧪 Input Validation

CipherForge includes validation for user input.

### Empty Input

The application rejects empty text input.

```text
[!] Input cannot be empty.
```

### Invalid Caesar Shift

The application requires a valid integer for the Caesar Cipher shift.

```text
[!] Invalid input. Please enter a valid integer.
```

### Invalid Vigenère Key

The Vigenère Cipher requires alphabetic characters.

For example:

```text
Key: 3
```

produces:

```text
[!] Error: Key must contain alphabetic characters only.
```

This prevents invalid key material from being used in the Vigenère algorithm.

---

## 🔬 Cryptographic Concepts Demonstrated

### Plaintext

The original readable message.

```text
Muhammad Zubair
```

### Ciphertext

The transformed output after encryption.

```text
Pxkdppdg Cxedlu
```

### Key

The value controlling the transformation.

For Caesar:

```text
Shift = 3
```

For Vigenère:

```text
Key = E
```

### Encryption

```text
Plaintext → Encryption → Ciphertext
```

### Decryption

```text
Ciphertext → Decryption → Plaintext
```

### Brute Force

Testing every possible key in a limited keyspace.

For the Caesar Cipher:

```text
26 possible shifts
```

---

## 🧪 Testing

The core encryption/decryption relationship is:

```text
decrypt(encrypt(plaintext, key), key) == plaintext
```

For example:

```text
Original Text
      ↓
Encryption
      ↓
Ciphertext
      ↓
Decryption
      ↓
Original Text
```

Future automated tests will cover:

* Caesar encryption
* Caesar decryption
* Vigenère encryption
* Vigenère decryption
* Encryption/decryption reversibility
* Uppercase characters
* Lowercase characters
* Spaces
* Numbers
* Special characters
* Negative Caesar shifts
* Large Caesar shifts
* Invalid Vigenère keys

---

## 🛡️ Security Considerations

CipherForge is an **educational cryptography project**.

The Caesar Cipher and Vigenère Cipher are classical algorithms and are **not secure for protecting real-world sensitive information**.

They are vulnerable to:

* Brute-force attacks
* Frequency analysis
* Known-plaintext attacks
* Statistical analysis
* Small keyspace attacks

Do not use these algorithms to protect:

* Passwords
* API keys
* Personal data
* Financial information
* Confidential communications
* Production systems

Modern applications should use established cryptographic standards and trusted cryptographic libraries.

---

## 📚 Educational Value

CipherForge demonstrates the difference between:

> **Understanding how cryptography works**

and:

> **Building secure modern cryptographic systems**

By implementing classical ciphers manually, the project provides practical experience with:

* Character transformations
* Modular arithmetic
* Key-based encryption
* Reversible algorithms
* Keyspace limitations
* Brute-force analysis
* Input validation
* Software modularity

---

## 🛣️ Roadmap

### Version 1.0.0 — Current

* [x] GitHub repository
* [x] Modular Python package structure
* [x] CipherForge ASCII banner
* [x] Interactive CLI
* [x] Caesar Cipher encryption
* [x] Caesar Cipher decryption
* [x] Custom numerical shift keys
* [x] Uppercase and lowercase support
* [x] Special character preservation
* [x] Vigenère Cipher encryption
* [x] Vigenère Cipher decryption
* [x] Alphabetic key validation
* [x] Caesar brute-force analysis
* [x] Input validation
* [x] Help menu
* [x] About section

### Version 1.1.0 — Planned

* [ ] Automated unit tests
* [ ] Improved test coverage
* [ ] Frequency analysis
* [ ] Improved cryptanalysis output
* [ ] Enhanced error handling

### Version 2.0.0 — Future

* [ ] File encryption and decryption
* [ ] Additional classical ciphers
* [ ] Educational cryptography visualizations
* [ ] Modern cryptography demonstrations
* [ ] Graphical user interface
* [ ] Cryptographic benchmarking

---

## 📈 Project Status

🟢 **Active Development**

CipherForge is currently a functional educational cryptography toolkit.

The current version provides:

* A working interactive CLI.
* Working Caesar Cipher encryption and decryption.
* Working Vigenère Cipher encryption and decryption.
* Vigenère key validation.
* Caesar brute-force analysis.
* A modular Python project structure.

Future development will focus on automated testing, additional cryptanalysis techniques, and expanded educational functionality.

---

## 🎓 Project Context

CipherForge was developed as part of **DecodeLabs Cybersecurity Project 2** to demonstrate fundamental encryption and decryption concepts using classical cryptography.

The project extends beyond a basic cipher implementation by including:

* Multiple classical cryptographic algorithms.
* Interactive command-line functionality.
* Brute-force analysis.
* Input validation.
* Modular application architecture.
* Cryptographic security analysis.

---

## ⚠️ Disclaimer

CipherForge is intended strictly for **educational and research purposes**.

The classical cryptographic algorithms implemented in this project are not suitable for protecting real-world confidential information.

Always use modern, peer-reviewed cryptographic standards and trusted implementations for real security applications.

---

## 👨‍💻 Author

### Muhammad Zubair

**Cybersecurity Student | SOC Analyst | Ethical Hacking Enthusiast**

### Areas of Interest

* Security Operations
* Threat Detection
* Network Security
* Ethical Hacking
* Cryptography
* Cybersecurity Research

---

## 📄 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for more information.

---

<p align="center">
  <b>Built for learning. Designed for experimentation. Developed for cybersecurity.</b>
</p>
