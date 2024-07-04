
def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def main():
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt a message? Enter 'q' to quit: ").lower()
        if choice == 'q':
            break
        if choice not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' for encrypt, 'd' for decrypt, or 'q' to quit.")
            continue
        
        message = input("Enter your message: ")
        shift = int(input("Enter shift value: "))
        
        if choice == 'e':
            encrypted_message = caesar_cipher(message, shift, mode='encrypt')
            print(f"Encrypted message: {encrypted_message}")
        else:
            decrypted_message = caesar_cipher(message, shift, mode='decrypt')
            print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
