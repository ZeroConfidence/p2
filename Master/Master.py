import Imagehandler
import Embedder
import decoder


def ConncetionCheck(Connect):
    if Connect == True:
        print("Master File has been connect succesfully")
    else:
        print("Master File failed to connect")

def Master_Encrypt(Stockbool,Stock_Number,Importet_Image,Message):
    if (stockbool == true):
        Stockimage = Imagesender(Stock_Number)
        return Carrier_embedder(Stockimage,Message)
    else:
        return Carrier_embedder(Importet_Image,Message)

def Master_Decrypt(Encrypted_image):#if you copy my homework change it a bit
    return Carrier_decoder(Encrypted_image)

