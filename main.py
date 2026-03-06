import hashlib
import time


def convert_text_to_sha1(text):
    digest = hashlib.sha1(text.encode()).hexdigest()
    return digest


def main():
    user_sha1 = input("Enter the SHA1 to Crack: ")
    cleaned_user_sha1 = user_sha1.strip().lower()

    attempts = 0
    start_time = time.time()

    with open('./passwords.txt') as f:
        for line in f:
            password = line.strip()
            converted_sha1 = convert_text_to_sha1(password)

            attempts += 1

            if cleaned_user_sha1 == converted_sha1:
                print(f"[SUCCESS] Password Found: {password}")
                print(f"Attempts: {attempts}")
                end_time = time.time()
                print(f"Time taken: {end_time - start_time:.4f} seconds")
                return

    end_time = time.time()
    print("[FAILED] Password not found")
    print(f"Attempts: {attempts}")
    print(f"Time taken: {end_time - start_time:.4f} seconds")


if __name__ == "__main__":
    main()