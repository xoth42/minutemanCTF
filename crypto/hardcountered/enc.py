myinput = bytearray.fromhex("07096d9d1f12a54a74e1c218d1b9e50a55ded1e806a616aeb6941cdb6be81f0b26e94899df9d6ea437a72db79b983832b3a958b97888b16b7b63b299b6a1671c256d07fd726a664b3ea584f2a1e9a28374048cef89489f5f7d")
#We now that xor can be reversed: if Plaintext ^ Secret = Ciphertext then we can get the secret key with CipherText ^ Plaintext = Secret
# Reads 32 bytes from a cryptographically secure random generator
plaintext = str.encode("{'username': 'Eve', 'type': 'user', 'secret': '2d063b0963bf646559948edfb9e4c3e4'}")
# print(len(plaintext))
secretlen = 64
ciphertext = myinput.copy()
# get secret
secret = ciphertext[:secretlen]
for i in range(0,min(len(plaintext),secretlen)):
    secret[i] = ciphertext[i] ^ plaintext[i]


# reverse message to get original
def decode(plain,secret):
    for i in range(0,len(plain)):
        plain[i] = plain[i] ^ secret[i%len(secret)]
    # print(plain)
    return plain

plain = decode(ciphertext,secret)
# print(plain[25:35]) 
# print(ciphertext)

# username start = 25
user_start = 25
user_end = 35
input_plain = bytearray(b"\': \'admin\',")
altered = myinput.copy()
input_enc = input_plain.copy()
for i in range(user_start,user_end+1):
    input_enc[i-user_start] = input_plain[i - user_start] ^ secret[i%len(secret)]
# go back to return altered original
altered =myinput.copy()
for i in range(user_start,user_start + len(input_enc)):
    altered[i] = input_enc[i - user_start]
print(altered.hex())

output = decode(altered,secret)
print (output)

# final = myinput[:25]
