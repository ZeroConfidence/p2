import Imagehandler                                                 #Imports Imagehandler file
import Embedder                                                     #Imports Embedder file
import Decoder                                                      #Imports Decoder file


def ConncetionCheck(Connect):
    if Connect == True:                                             #checks if the master file connected to the js translater file
        print("Master File has been connect succesfully")
    else:                                                           #if connection failed
        print("Master File failed to connect")

def Master_Encrypt(Stockbool,Stock_Number,Imported_Image,Message):  #Master encrypter calls for stockbool, Stock_number, Imported_Image and the message
    if (stockbool == true):                                         #If the stockbool is true
        Stockimage = Imagesender(Stock_Number)                      #then stockimage calls the imagesender file with the stock_number as an input
        return Carrier_embedder(Stockimage,Message)                 #returns the called carrier_embedder with the stockimage and messages as inputs
    else:                                                           #if else
        return Carrier_embedder(Imported_Image,Message)             #returns the called carrier_embedder with the imported_image and messages as inputs

def Master_Decrypt(Encrypted_image):                                #Master decrypted calls for the encrypted image
    return Carrier_decoder(Encrypted_image)                         #returns the called Carrier decoder with the encrypted image as input

