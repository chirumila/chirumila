from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    image = Image.open(image_path)
    pixels = np.array(image)
    encrypted_pixels = (pixels + key) % 256  # Basic mathematical operation
    encrypted_image = Image.fromarray(encrypted_pixels.astype(np.uint8))
    encrypted_image.save("encrypted_image.png")
    return "encrypted_image.png"

def decrypt_image(encrypted_image_path, key):
    encrypted_image = Image.open(encrypted_image_path)
    encrypted_pixels = np.array(encrypted_image)
    decrypted_pixels = (encrypted_pixels - key) % 256  # Reverse operation
    decrypted_image = Image.fromarray(decrypted_pixels.astype(np.uint8))
    decrypted_image.save("decrypted_image.png")
    return "decrypted_image.png"

def main():
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt an image? Enter 'q' to quit: ").lower()
        if choice == 'q':
            break
        if choice not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' for encrypt, 'd' for decrypt, or 'q' to quit.")
            continue
        
        image_path = input("Enter the path to your image: ")
        key = int(input("Enter a key (integer value): "))
        
        if choice == 'e':
            encrypted_image_path = encrypt_image(image_path, key)
            print(f"Encrypted image saved as: {encrypted_image_path}")
        else:
            decrypted_image_path = decrypt_image(image_path, key)
            print(f"Decrypted image saved as: {decrypted_image_path}")

if __name__ == "__main__":
    main()
