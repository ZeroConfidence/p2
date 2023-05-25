#from Imagehandler import ImageSender                                               #Imports Imagehandler file
from Embedder     import Carrier_embedder                                                    #Imports Embedder file
from decoder      import Carrier_decoder                                                     #Imports Decoder file
import json                                                             #Imports json lib
from base64 import b64encode,b64decode                                                         #Imports Base64 lib
from flask import Flask, request, send_file, Response,jsonify
from flask_cors import CORS
from io import BytesIO
from PIL import Image
import io



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
    #get the data from the website's form data
    message = request.form['message']
    key = request.form['key']
    image = request.files['Base_File'].read()

    image_reworked = Image.open(BytesIO(image))#opens the image data as an image
    
    encodeimage = Carrier_embedder(image_reworked,message,key) #embeds messag into image
    
    #converts encoded image to PNG format
    with io.BytesIO() as output: 
        encodeimage.save(output,format='PNG')
        encoded_image_reworked = output.getvalue()
    return send_file(io.BytesIO(encoded_image_reworked),mimetype='image/png')
    



       


@app.route('/api/Master_Decrypt',methods = ["POST"])
def Master_Decrypt():                                    #Master decrypted calls for the encrypted image
    #get the data from the website's form data
    image = request.files['decodeFile'].read()#use .read to save image in memory
    key = request.form['key']

    image_reworked = Image.open(BytesIO(image))#opens the image data as an image
    
    message = Carrier_decoder(image_reworked,key)#extractes message from image
    
    return jsonify(message)#returns message as json




    

if __name__ == '__main__':
    app.debug = True
    app.run(debug=True) #nice
