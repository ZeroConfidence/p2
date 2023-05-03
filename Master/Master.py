import Imagehandler                                                 #Imports Imagehandler file
import Embedder                                                     #Imports Embedder file
import Decoder                                                      #Imports Decoder file
import json                                                         #Imports json lib
import base64                                                       #Imports Base64 lib


def rest_api():
    x
def JSON_Create():
    Website_Package_Py = {                                          #Creates Python dictionary with inputs:
        "b64_image": "x",                                           #the B64 image as a string element
        "key":"x",                                                  #key as a string element
        "msg":"x",                                                  #message that the user wishes to encode, as a string
        "stock_num":0,                                              #the stock image's number, this is an integer value
        "image":"x"                                                 #the base image as a string
    }
    return(Website_package)                                         #returns the dictionary

def Image_Converter(Image):
    Bin_Image = bytes(Image)                        #converts the image into binary
    B64_Image = b64encode(Bin_Image, altchars=none) #converts the binary string into base64
    return(B64_Image)


def JSON_Sender(Website_Package_Py,msg,Key,Image,B64_Image,Stock_num):
    Website_Package_Py["b64_image"] = B64_Image                         #changes the dict value b64_image to the imported B64_Image variable
    Website_Package_Py["key"] = Key                                     #changes the dict value key to the imported key variable
    Website_Package_Py["msg"] = msg                                     #changes the dict value msg to the imported msg variable
    Website_Package_Py["image"]= Image                                  #changes the dict value image to the imported image variable
    Website_Package_Py["stock_num"]=Stock_num                           #changes the dict value stock_num to the imported stock_num variable
    Website_Package = json.dumps(Website_Package_Py, ensure_ascii=false)#dumps the python dict into a json file, retaining all character due to ensure_ascii=false
    return(Website_Package)

def JSON_receiver(JSON):
    JSON_Unpack = json.loads(JSON)
    Return(JSON_Unpack)


def Conncetion_Check(Connect):
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

