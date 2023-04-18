from PIL import Image
"""
This code is designed to take a a message and encode it into a selected image using the LSB method
It then returns the encoded image
"""


def set_lsb(n, bit): # changes the last bit of the given integer n to that of the binary bit
   
    if bit == '1':
        return (n | 1)
    else:
        return (n & ~1)

def Carrier_embedder(Carrier,Message):
    image = Image.open(Carrier)

    message_binary = ''.join(format(ord(c),'08b')for c in Message) #converts the message into it's ASCII equivalent and then converts that into 8 bit binary and joins it into a string
    
    message_length_binary = bin(len(Message))[2:] #takes the length of message and convert in into binary and removed the '0b' prefix
    message_length_binary = '{:0>16}'.format(message_length_binary)# pads the binary message_length_binary with 0 until it fills 16 bits

    pixels = image.load()
    Bits_encoded = 0 #used to keep track of number of encoded bits

    #for loops used to keep the operations inside the image boundries
    for i in range(image.size[0]):
        for k in range(image.size[1]):
            red, green, blue = pixels[i, k]

            #while loop encodes the first 16 bits with the length of the message
            while Bits_encoded < 16:
                
                red = set_lsb(red,message_length_binary[Bits_encoded]) 
                Bits_encoded += 1

                if Bits_encoded==16:
                    break

                green = set_lsb(green,message_length_binary[Bits_encoded]) 
                Bits_encoded += 1

                blue = set_lsb(blue,message_length_binary[Bits_encoded]) 
                Bits_encoded += 1


            #code does these operations only if entire message has not been encoded and not before the first 16 bits have been encoded
            if Bits_encoded < len(message_binary+16) & Bits_encoded > 16:
                red = set_lsb(red,(message_binary[Bits_encoded-16]))#encodes red channel for current pixel 
                Bits_encoded += 1

            if Bits_encoded < len(message_binary+16) & Bits_encoded > 16:
                green = set_lsb(green,(message_binary[Bits_encoded-16]))#encodes green channel for current pixel 
                Bits_encoded += 1

            if Bits_encoded < len(message_binary+16) & Bits_encoded > 16:
                blue = set_lsb(blue,(message_binary[Bits_encoded-16]))#encodes blue channel for current pixel 
                Bits_encoded += 1

            pixels[i, k] = (red, green, blue)

            if Bits_encoded >= len(message_binary+16) & Bits_encoded > 16: #once entire message is encoded returns modified image  
                return image