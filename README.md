# Password Hash Cracker 🔐

A simple Python tool that performs a **dictionary attack** to crack SHA1 password hashes.

## Features

* Crack SHA1 password hashes
* Dictionary attack using a wordlist
* Shows number of attempts
* Displays execution time

## How it works

The program reads passwords from a wordlist and generates their SHA1 hashes.
If the generated hash matches the target hash, the password is found.

## Usage

Run the program:

```
python main.py
```

Enter the SHA1 hash you want to crack:

```
Enter the SHA1 to Crack:
```

Example output:

```
[SUCCESS] Password Found: secure123
Attempts: 34
Time taken: 0.0213 seconds
```

## Project Structure

```
Password-Hash-Cracker
│
├── main.py
├── passwords.txt
└── README.md
```

## Educational Purpose

This project demonstrates how **dictionary attacks work** and why strong passwords and hashing algorithms are important in cybersecurity.
