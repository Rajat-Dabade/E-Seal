import os, random, struct
from Crypto.Cipher import AES
from Crypto import Random
import rsa

def decrypt_file(key, in_filename, out_filename=None, chunksize=24*1024):
    """ Decrypts a file using AES (CBC mode) with the
        given key. Parameters are similar to encrypt_file,
        with one difference: out_filename, if not supplied
        will be in_filename without its last extension
        (i.e. if in_filename is 'aaa.zip.enc' then
        out_filename will be 'aaa.zip')
    """
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]

    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(origsize)

def key_to_file(key,out_filename=None):
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]
    outfile = open(out_filename, 'wb')
    outfile.write(key)

# with open('H:\\Hackathon\\EncryptedAESKey.txt',mode='rb') as keyfile:
#     Encaeskey = keyfile.read()

# aeskey = rsa.decrypt(Encaeskey,privkey)

# decrypt_file(aeskey,'C:\\Users\\Aniket\\Desktop\\Presentation.pptx.enc','C:\\Users\\Aniket\\Desktop\\Presentation_decry.pptx')
