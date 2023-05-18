from Crypto.Cipher import AES

key = b'Sixteen byte key'

def do_encrypt(msg):
    obj = AES.new(key, AES.MODE_CBC, 'This is an IV456')

    while len(bytes(msg, encoding='utf-8')) % 16 != 0:
        msg = msg + ' '
    ciphertext = obj.encrypt(msg)

    return ciphertext

def do_decrypt(ciphertext):
    obj2 = AES.new(key, AES.MODE_CBC, 'This is an IV456')

    message = obj2.decrypt(ciphertext)
    return message