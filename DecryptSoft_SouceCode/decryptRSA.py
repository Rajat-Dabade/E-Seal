import os, random, struct
from Crypto.Cipher import AES
from Crypto import Random
import rsa
import sys
import pds.checkDevice as cd

def decryptRSA(symKeyPath):
    key="""-----BEGIN RSA PRIVATE KEY-----
MIICXwIBAAKBgQDdrimv1+uFLpaZBo/eUOE1WzAx4r7f91/uJTI8cF6h6WZN6hZx
zVFDUIM43YNX2KXRgoMOkZYXaHD9VQH0eCsR5BWLacPCbyuHLvMjB6QnNLtZKAfC
gTx326Nb/v5+FycVMZEB1NFbPNyv2PNlMfFC6X6/DAYtv8Isjb1HMA7BpQIDAQAB
AoGAM2yqiPs6zItxLhCCoVz70WfU902VX9k/7Lu+Op0Kpt7A98Qc7stlVYtA1Zk1
VdSRKtfu1RtayRVWWL42WrFw2eNOSEB1KIDf1AsvTvs26oZsc3ghvchV+KldVEkA
WSuSkktaT+HDzBDZnZ6GfwSRpNtg5/9vJu0eNpQNGMh3nOUCRQD62tFHq9+Zvm6T
GqolFl1ejDy0p4ih5MnZl79B5Ks0JrkKwa29G81w17aCMAqjjBzDNBClpauI/NL3
fFCg8PBOIK+H+wI9AOI6KCnOWjMoJFls1mWN0Ab//yotxoHra/QdxwFjCBBUljEP
oWlJPMFj0mN2GPltyj4iX08zCTsm3m6K3wJEJFAuwXBI8wmVGihe/vVo2Ln2Q7SI
296xtZT488H1YpxEZyE4VErFB5PCcMAhmiE7PKq5yjDcTv1CUN8nENUwBC9JGacC
PALzjUiWV5jpQigkgluK0Rb2Sgbr1/Yj8yGZLdp3x0gnQlpbgNiVywQe4ETJ6qN+
ajALVMD8wncSF77LcwJEbwCUGUqplZ0rm8k7OgrNUU6t0C9eRtYoRlsk94npPUt5
hvrHp26MMWAkCbCRPQSyS0Ty7sVb0uj6R6nUn8Ld6ELicn8=
-----END RSA PRIVATE KEY-----
"""

    f = open(cd.getPath()+'temp.pem','wb')
    f.write(key)
    f.close()

    with open(cd.getPath()+'temp.pem', mode='rb') as privatefile:
        key = privatefile.read()

        priv_key = rsa.PrivateKey.load_pkcs1(key)

    with open(symKeyPath, mode='rb') as encfile:
        enckey = encfile.read()

    message = rsa.decrypt(enckey,priv_key)
    os.remove(cd.getPath()+'temp.pem')
    return message

