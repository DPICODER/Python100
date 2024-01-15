from art import logo

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z',
            'a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']
print(logo)

def cesar(Cyper_Type , shiftby , text):
    end_text = ""
    if Cyper_Type == "decode" or Cyper_Type == "Decode":
            shiftby *= -1
    for letter in text:
        if letter in alphabet:
            pos = alphabet.index(letter)
            newpos = pos + shiftby
            end_text += alphabet[newpos]
        else:
             end_text += letter


    print(f"The {Cyper_Type} text is {end_text}")


to_continue = True

while to_continue:
    Code_Type = input("Type : 'Encode' to Encrypt , Type : 'decode' to Decrypt : \n")
    input_text = input(" Enter Message :\n").lower()
    Letter_shift = int(input(" Type The Shift number :\n")) 

    Letter_shift = Letter_shift % 26
    cesar(Cyper_Type=Code_Type , text=input_text , shiftby=Letter_shift)
    
    result = input("Type 'yes' if want to continue . Or Type 'no' to exit .\n")
    if result == 'no':
         to_continue = False
         print("DONE !!!")





















#---------------Different Implementation styles---------------------- 


# def cesar_if based(Cyper_Type , text , shiftby):
#     if Cyper_Type == 'encode' or Cyper_Type == 'Encode':
#         cipher_text = ""
#         for letter in text:
#             pos = alphabet.index(letter)
#             new_pos = pos + shiftby
#             new_letter = alphabet[new_pos]
#             cipher_text += new_letter
#         print(f"The Encoded Message is {cipher_text}\n")
#     elif Cyper_Type == 'decode' or Cyper_Type == 'Decode':
#         plaintext = ""
#         for letter in text:
#             pos = alphabet.index(letter)
#             new_pos = pos - shiftby
#             new_letter = alphabet[new_pos]
#             plaintext += new_letter
#         print(f"The Decoded Message is {plaintext}\n")



# def Encrypt(plaintext , shiftval):

#     
#     for letter in plaintext:
#         pos = alphabet.index(letter)
#         new_pos = pos + shiftval
#         new_letter = alphabet[new_pos]
#         cipher_text += new_letter

#     print(f"The Encoded Message is {cipher_text}\n")

# def Decrypt(ciphertext , shiftamount):

#     plaintext = ""
#     for letter in ciphertext:
#         pos = alphabet.index(letter)
#         new_pos = pos - shiftamount
#         new_letter = alphabet[new_pos]
#         plaintext += new_letter

#     print(f"The Decoded Message is {plaintext}\n")

# if Cyper_Type == "encode" or text == "Encode":
#     Encrypt(plaintext=text,shiftval=shiftby)
# elif Cyper_Type == "decode" or text == "Decode":
#     Decrypt(ciphertext=text,shiftamount=shiftby)
# else:
#     print("Enter a Valid type Again")