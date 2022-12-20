import uuid
import hashlib
from Crypto.Cipher import AES
from os import urandom

class Enc_Dec:

    # Initialization Vector
    def get_iv(self):
        return urandom(16)

    # Hashing the Key
    def SHA(self,key):
        salt = uuid.uuid4().hex
        sha_sig = hashlib.sha256(salt.encode() + key.encode()).hexdigest()
        # Taking first 16 characters of the SHA256 output
        sha_sig = sha_sig[:16]
        # Converting those 16 characters into bytes
        key = sha_sig.encode("UTF-8")
        return key

    # Encryption Method
    def EncryptionEngine(self,key, iv, message):
        msg_len = len(message)
        # print(msg_len)

        # Checking the message length
        if msg_len % 16 != 0:
            # adding space if any message len is not a multiple of 16
            message += ' ' * (16 - msg_len % 16)
        # print(len(message))

        #Encrypting the message
        obj = AES.new(key, AES.MODE_CBC, iv)
        encrypted_text = obj.encrypt(message.encode("UTF-8"))
        # print("The encrypted text:", encrypted_text)
        return encrypted_text

    # Decryption Method
    def DecryptionEngine(self,key, iv, encryption):
        rev_obj = AES.new(key, AES.MODE_CBC, iv)
        decrypted_text = rev_obj.decrypt(encryption).decode("utf-8")
        # print("The decrypted text:", decrypted_text.decode('utf-8'))
        return decrypted_text



    

# obj = Enc_Dec()

# key = obj.SHA("ProjectSwans")
# msg = "Hello. How are You?"
# iv = obj.get_iv()
# enc_text = obj.EncryptionEngine(key,iv,msg)
# print(enc_text)

# dec_text = obj.DecryptionEngine(key,iv,enc_text)
# print(dec_text)
