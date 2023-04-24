from Imagehandler import ImageSender                                #Imports Imagehandler file
from Embedder import Carrier_embedder                               #Imports Embedder file
from decoder import Carrier_decoder                                 #Imports Decoder file


def ConncetionCheck(Connect):
    if Connect == True:                                             #checks if the master file connected to the js translater file
        print("Master File has been connect succesfully")
    else:                                                           #if connection failed
        print("Master File failed to connect")

def Master_Encrypt(Stockbool,Stock_Number,Imported_Image,Message,key):  #Master encrypter calls for stockbool, Stock_number, Imported_Image and the message
    if (Stockbool == 1):                                            #If the stockbool is true
        Stockimage = ImageSender(Stock_Number)                      #then stockimage calls the imagesender file with the stock_number as an input
        return Carrier_embedder(Stockimage,Message,key)                 #returns the called carrier_embedder with the stockimage and messages as inputs
    else:                                                           #if else
        return Carrier_embedder(Imported_Image,Message,key)             #returns the called carrier_embedder with the imported_image and messages as inputs

def Master_Decrypt(Encrypted_image,key):                                #Master decrypted calls for the encrypted image
    return Carrier_decoder(Encrypted_image,key)                         #returns the called Carrier decoder with the encrypted image as input

