# Caesar Cipher

The Caesar Cipher is a basic encryption technique that shifts the letters of the alphabet by a fixed number of positions. It is a type of substitution cipher where each letter in the plaintext is replaced by a letter some fixed number of positions down or up the alphabet.

## Usage :

To use the Caesar Cipher :

1. Choose a shift value (key). This is the number of positions each letter of the plaintext will be shifted.
2. Encrypt the message by replacing each letter with the letter that is the specified number of positions down the alphabet.
3. Decrypt the message by shifting the letters in the reverse direction.

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
```
## Notes
1 . The Caesar Cipher is a symmetric key algorithm, meaning the same key is used for both encryption and decryption.
2 . It is a simple and easily breakable encryption method, and it's mainly used for educational purposes or in situations where strong security is not required.

