import sympy

print("please specify 'a' such that - GCD of 'a' & '26' should be 1 & should be in range of 0 to 25")
print("To Encrypt message - 1 \n"
      "To Decrypt message - 2")

while 1:
    message = input("Message:- ")
    str = message.lower().replace(" ", "")
    alphabets = list(map(chr, range(97, 123)))
    while 1:
        a = int(input("a = "))
        b = int(input("b = "))
        if 0 < a < 26:
            i = 1
            while i <= 26:
                if a % i == 0 and 26 % i == 0:
                    gcd = i
                i = i + 1
            break
        else:
            print("a is not between 0-25")
            print("please specify a & b again")

    def affine_encrypt():
        plaintext = list(str)
        length = len(plaintext)
        encrypted_msg = []

        if gcd != 1:
            print("GCD of 'a' & '26' is not 1")
        else:
            for l in range(0, length):
                pos = alphabets.index(plaintext[l])
                new_alphabet = ((a * pos) + b) % 26
                encrypted_msg.append(alphabets[new_alphabet])
            print("encrypted text = " + "".join(encrypted_msg))
        return encrypted_msg

    def affine_decrypt():
        ciphertext = list(str)
        length = len(ciphertext)
        decrypted_msg = []

        if gcd != 1:
            print("GCD of 'a' & '26' is not 1")
        else:
            for l in range(0, length):
                a1 = sympy.mod_inverse(a, 26)
                pos = alphabets.index(ciphertext[l])
                new_alphabet = (a1 * (pos - b)) % 26
                decrypted_msg.append(alphabets[new_alphabet])
            print("decrypted text = " + "".join(decrypted_msg))
        return decrypted_msg

    def default():
        print("invalid option!")

    x = int(input("Specify Option:- "))
    if x == 1:
        affine_encrypt()
    elif x == 2:
        affine_decrypt()
    else:
        default()