from Embedder     import Carrier_embedder  #Imports Embedder file
from decoder      import Carrier_decoder   #Imports Decoder file
import json                                #Imports json lib
from flask import Flask, request, send_file, Response,jsonify
from flask_cors import CORS
from io import BytesIO
from PIL import Image
import io

app = Flask(__name__)
CORS(app)

@app.route('/api/Master_Encrypt',methods=['POST'])
def Master_Encrypt():  #Master encrypter calls for stockbool, Stock_number, Imported_Image and the message
    message = request.form['message']
    key = request.form['key']
    image = request.files['Base_File'].read()
    image_reworked = Image.open(BytesIO(image))
    
    encodeimage = Carrier_embedder(image_reworked,message,key)
    with io.BytesIO() as output:
        encodeimage.save(output,format='PNG')
        encoded_image_reworked = output.getvalue()
    return send_file(io.BytesIO(encoded_image_reworked),mimetype='image/png')
    
@app.route('/api/Master_Decrypt',methods = ["POST"])
def Master_Decrypt():                                    #Master decrypted calls for the encrypted image
    image = request.files['decodeFile'].read()
    key = request.form['key']
    image_reworked = Image.open(BytesIO(image))
    message = Carrier_decoder(image_reworked,key)
    
    return jsonify(message)

if __name__ == '__main__':
    app.debug = True
    app.run(debug=True) #nice
