import tkFileDialog
import pds.checkDevice as cd
import easygui as eg
import CryptoLocal.DecryptFile as df
import decryptRSA as drsa

def gui():
    while(True):
        if (cd.check()==1):
            buttons = ['Upload Encrypted File','Close']
            replay= eg.buttonbox("Please Click Below to Upload Encrypted File",choices=buttons)
            if(replay=='Close'):
                break
            encFilePath = tkFileDialog.askopenfilename()
            buttons = ['Upload Provided Key','Close']
            replay= eg.buttonbox("Please Click Below to Upload Key",choices=buttons)
            if(replay=='Close'):
                break
            keyPath = tkFileDialog.askopenfilename()
            
            # key = open(keyPath,'r')
            # aesKey=key.read()
            # key.close()
            # buttons = ['Destination Path to store Decrypted File','Close']
            # replay= eg.buttonbox("Please Click Below to Upload Key",choices=buttons)
            # if(replay=='Close'):
            #     break
            try:
                aesKey=drsa.decryptRSA(keyPath)
                df.decrypt_file(aesKey,encFilePath)
                replay=eg.buttonbox("Your File Decrypted Succesfully",choices=['Close'])
                if(replay=='Close'):
                    break
            except:
                buttons = ['Retry','Close']
                replay= eg.buttonbox("Could Not Decrypt The file please recheck Key.\nYour Key:"+keyPath,choices=buttons)
                if(replay=='Close'):
                    break
                else:
                    continue
            # decFile = tkFileDialog.asksaveasfile(mode='w', defaultextension="")
            # decFile.write()
            # decFile.close()
        else:
            buttons = ['Try Again','Close']
            replay= eg.buttonbox("Could not find the hardware key.Please Attach The Hardware key. ",choices=buttons)
            if(replay == 'Close'):
                break
    return
