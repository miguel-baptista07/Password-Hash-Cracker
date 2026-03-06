# Password Hash Cracker

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Cybersecurity-red?style=for-the-badge)

A Python tool that performs a **dictionary attack** against SHA1 password hashes —
built to understand how weak passwords and unsalted hashes can be compromised.

---

## Features

- Dictionary attack using a custom wordlist
- SHA1 hash generation and comparison
- Reports number of attempts and execution time
- Clean success/failure output

---

## Usage
```bash
python main.py
```

Enter the SHA1 hash you want to crack:
```
Enter the SHA1 to Crack: aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d
```

Example output:
```
[SUCCESS] Password Found: hello
Attempts: 34
Time taken: 0.0213 seconds
```

---

## How It Works

The tool reads each word from `passwords.txt`, computes its SHA1 hash using
Python's `hashlib` module, and compares it against the target hash.
If a match is found, the original password is recovered.

This demonstrates why **unsalted SHA1 hashes are insecure** — a simple wordlist
is often enough to reverse them.

---

## Project Structure
```
Password-Hash-Cracker/
├── main.py           # Core cracker logic
├── passwords.txt     # Wordlist for dictionary attack
└── README.md
```

---

## What I Learned

- How SHA1 hashing works and why it is considered weak for password storage
- The mechanics of a dictionary attack vs brute-force
- Why password salting is essential to prevent precomputed hash attacks
- Practical use of Python's `hashlib` module

---

## ⚠️ Disclaimer

This tool is intended for **educational purposes only**.  
Only use it on hashes you own or have **explicit permission** to test.  
Unauthorized use against real systems may be illegal.

---

## License

MIT License