import os, random, struct
from Crypto.Cipher import AES
from Crypto import Random
import rsa
import sys

def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
    """ Encrypts a file using AES (CBC mode) with the
        given key.

        key:
            The encryption key - a string that must be
            either 16, 24 or 32 bytes long. Longer keys
            are more secure.

        in_filename:
            Name of the input file

        out_filename:
            If None, '<in_filename>.enc' will be used.

        chunksize:
            Sets the size of the chunk which the function
            uses to read and encrypt the file. Larger chunk
            sizes can be faster for some files and machines.
            chunksize must be divisible by 16.
    """
    if not out_filename:
        out_filename = in_filename + '.enc'

    iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))

def key_to_file(key,out_filename=None):
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]
    outfile = open(out_filename, 'wb')
    outfile.write(key)
                

aeskey = Random.new().read(32)
encrypt_file(aeskey,sys.argv[1])
# keyname = os.path.dirname(os.path.realpath(__file__))+'/Upload/key_'+(os.path.splitext(sys.argv[2]))[0]+'.txt'
# key_to_file(aeskey,keyname)

with open("C:\\Users\\ank13\\Desktop\\Coep_hack\\DecryptSoft_SouceCode\\CryptoLocal\\publickey.pem", mode='rb') as publicfile:
    keydata = publicfile.read()
    
pubkey = rsa.PublicKey.load_pkcs1(keydata)
enc_aes_key = rsa.encrypt(aeskey,pubkey)

fil = open("C:\\xampp\\htdocs\\authentication\\Upload\\RSA_KEY_"+(os.path.splitext(sys.argv[2]))[0]+'.txt','wb')
fil.write(enc_aes_key)


