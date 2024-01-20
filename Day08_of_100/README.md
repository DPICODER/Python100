# Caesar Cipher

The Caesar Cipher is a basic encryption technique that shifts the letters of the alphabet by a fixed number of positions. It is a type of substitution cipher where each letter in the plaintext is replaced by a letter some fixed number of positions down or up the alphabet.

### Getting Started
To use the Caesar Cipher program, run the provided Python script. Follow the on-screen instructions to select the operation (encode or decode), enter the message, and specify the shift number.

```python
python main.py
```

To use the Caesar Cipher :

1. Choose a shift value (key). This is the number of positions each letter of the plaintext will be shifted.
2. Encrypt the message by replacing each letter with the letter that is the specified number of positions down the alphabet.
3. Decrypt the message by shifting the letters in the reverse direction.

### Available Operations
- **Encode:** Encrypts the message using the Caesar Cipher.
- **Decode:** Decrypts the message using the Caesar Cipher.

### How It Works
1. Choose the operation: 'encode' to encrypt or 'decode' to decrypt.
2. Enter the message you want to encrypt or decrypt.
3. Specify the shift number (positive integer) for the Caesar Cipher.
4. View the result of the operation.

### Functions
- `cesar(Cyper_Type, shiftby, text)`: Performs the Caesar Cipher encryption or decryption based on the specified operation and shift value.

### Encryption and Decryption
The program supports both encryption (encoding) and decryption (decoding) of messages. The result will be displayed on the screen.


## Example

### Encryption

```plaintext
Original:    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Shift by 3:   D E F G H I J K L M N O P Q R S T U V W X Y Z A B C

```

### Encrypting "HELLO" with a shift of 3:
```
Plaintext:   H E L L O
Ciphertext:  K H O O R
```

## Decryption
### Decrypting "KHOOR" with a shift of 3:

```
Ciphertext:  K H O O R
Plaintext:   H E L L O

### Performing Another Operation
After completing an operation, you have the option to continue with another encryption or decryption or exit the program.
```

## Notes
1 . The Caesar Cipher is a symmetric key algorithm, meaning the same key is used for both encryption and decryption.
2 . It is a simple and easily breakable encryption method, and it's mainly used for educational purposes or in situations where strong security is not required.


### Enjoy Using the Caesar Cipher!
Thank you for using the Caesar Cipher program! Whether you're securing messages or decoding secret texts, we hope this tool serves your needs. If you have any feedback or suggestions, feel free to share them. Happy encoding and decoding!
