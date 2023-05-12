from Imagehandler import ImageSender                                               #Imports Imagehandler file
from Embedder     import Carrier_embedder                                                    #Imports Embedder file
from decoder      import Carrier_decoder                                                     #Imports Decoder file
import json                                                             #Imports json lib
from base64 import b64encode,b64decode                                                         #Imports Base64 lib
from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import io
from PIL import Image


app = Flask(__name__)
CORS(app)

    
def JSON_Create(data1,data2):
    Website_Package_Py = {                                              #Creates Python dictionary with inputs:
        "b64_image":data1,                                               #the B64 image as a string element                                                      #key as a string element
        "msg":data2,                                                      #message that the user wishes to encode, as a string
    }
    return Website_Package_Py                                             #returns the dictionary

def Image_Converter_Decode(Encrypted_image):
    Bin_Image = b64decode(Encrypted_image,altchars=None)                      #converts the base64 string into binary
    #Byte_Image = bytes(str(Bin_Image),'utf-8')                               #converts the binary string into a byte grouping
    IO_Image = io.BytesIO(Bin_Image)                                    #converts the byte grouping into a IO string
    image = Image.open(IO_Image)                                        #open the IO string with Pillow
    return(image)


def Image_Converter_Encode(Image):
    Bin_Image = bytes(Image)                                            #converts the image into binary
    B64_Image = b64encode(Bin_Image, altchars=None)                     #converts the binary string into base64
    return B64_Image


def JSON_Sender(Website_Package_Py,msg,Key,Image,B64_Image,Stock_num):
    Website_Package_Py["b64_image"] = B64_Image                         #changes the dict value b64_image to the imported B64_Image variable
    Website_Package_Py["msg"] = msg                                     #changes the dict value msg to the imported msg variable
    Website_Package_Py = json.dumps(Website_Package_Py, ensure_ascii=True)#dumps the python dict into a json file, retaining all character due to ensure_ascii=false
    return Website_Package_Py

def JSON_receiver(JSON):
    JSON_Unpack = json.loads(JSON)
    return JSON_Unpack


def Conncetion_Check(Connect):
    if Connect == True:                                             #checks if the master file connected to the js translater file
        print("Master File has been connect succesfully")
    else:                                                           #if connection failed
        print("Master File failed to connect")

@app.route('/api/Master_Encrypt',methods=['POST'])
def Master_Encrypt():  #Master encrypter calls for stockbool, Stock_number, Imported_Image and the message
    
        json_from_js = request.get_json()
            
        imported_image = json_from_js['imported_image']
        message = json_from_js['msg']
        key = json_from_js['key']
        
        imported_image = Image_Converter_Decode(imported_image)
        encoded_image = Carrier_embedder(imported_image,message,key)

        b64_image = Image_Converter_Encode(encoded_image)
        response = {'b64_image':b64_image.decode('utf-8')}
        
        return jsonify(response)           


@app.route('/api/Master_Decrypt')
def Master_Decrypt():                                    #Master decrypted calls for the encrypted image
    json_from_js = request.json
    Encrypted_image = Image_Converter_Decode(json_from_js['Encrypted_image'])
    key = json_from_js['key']


    return Carrier_decoder(Encrypted_image,key)                         #returns the called Carrier decoder with the encrypted image as input

if __name__ == '__main__':
    app.debug = True
    app.run(debug=True) #nice
