secret_message = "This is most deffinitely NOT a secret message 4 (p.s. vigenere ciphers are better)"
number = 69
character_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"



def caesar_cipher(text: str, shift: int) -> str:
    result = ""
    
    for char in text:
        if char in character_list:
            result += character_list[(character_list.index(char) + shift) % 62]
        else:
            result += char

    return result




hidden_message = caesar_cipher(secret_message, number)
def caesar_decipher(text: str, shift: int) -> str:
    
    result = ""
    
    for char in text:
        if char in character_list:
            result += character_list[(character_list.index(char) - shift) % 62]
        else:
            result += char

    return result



def brute_force_caesar_decipher(text: str):
    for shift in range(len(character_list)):
        deciphered_text = caesar_decipher(text, shift)
        print(f"Shift {shift}: {deciphered_text}")


print(f"Encrypted message: {hidden_message}")

brute_force_caesar_decipher(hidden_message)
