def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            # Determine the appropriate case (uppercase or lowercase)
            base = ord('A') if char.isupper() else ord('a')
            # Perform the shift while keeping within the bounds of A-Z and a-z
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text += encrypted_char
        else:
            # If the character is not a letter, keep it unchanged
            encrypted_text += char
    return encrypted_text

# Example usage:
plaintext = "Hello, World!"
shift = 3
encrypted_text = caesar_cipher(plaintext, shift)
print("Original:", plaintext)
print("Encrypted:", encrypted_text)
