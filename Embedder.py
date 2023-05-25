from PIL import Image
import random
import math
"""
This code is designed to take a a message and encode it into a selected image using the LSB method
It then returns the encoded image
"""


def set_lsb(n, bit): # changes the last bit of the given integer n to that of the binary bit
   
    if bit == '1':
        return (n | 1) #does binary or operation on the given color value and 1
    else:
        return (n & ~1) #does binary and operation on the given color value and not 1
   

def Carrier_embedder(Carrier,Message,key):
    image = Carrier #Image.open(Carrier)
    testbool = False #used to skip to next pixel after encoding length of message
    message_binary = ''.join(format(ord(c),'08b')for c in Message) #converts the message into it's ASCII equivalent and then converts that into 8 bit binary and joins it into a string
    max_bytes = ((image.size[0] * image.size[1] * 3)/8) #finds the maximum number of encoded bytes
    binary_length_max_bytes = math.ceil(math.log2(max_bytes)) #finds the length of the binary prepresentation of max_bytes
    
    message_length_binary = bin(len(Message))[2:] #takes the length of message and convert in into binary and removed the '0b' prefix
    
    
    message_length_binary = message_length_binary.zfill(binary_length_max_bytes) #pads the binary message_length_binary with 0 until it fills tha same amound of bits as max_bytes
    

    pixels = image.load()
    Bits_encoded = 0 #used to keep track of number of encoded bits

    
    random.seed(key) # sets key as the seed for the psudo-random number generator 
    Pixel_Coordinates = [(x,y)for x in range(image.size[0]) for y in range(image.size[1])] #loads the coordinates for he pixels into the pixel_coordinate variable 
    random.shuffle(Pixel_Coordinates) #shuffles around the x and y cordinates for pixel_coordinates to make a new psudorandom sequence based on the given key
    
    for x,y in Pixel_Coordinates:
        red, green, blue, alpha = pixels[x, y]
        if alpha == 0:
            alpha = 1 #if alpha is 0 it turns pixel white, lmao lies any alpha breaks the reader part
        continue_counter = 0
        #while loop encodes the first bits with the length of the message
        if Bits_encoded < binary_length_max_bytes:
            
              
            red = set_lsb(red,message_length_binary[Bits_encoded]) 
            
            Bits_encoded += 1
            continue_counter =1
            
            
        if Bits_encoded < binary_length_max_bytes:    

            green = set_lsb(green,message_length_binary[Bits_encoded])
            
            Bits_encoded += 1
            
           
        if Bits_encoded < binary_length_max_bytes:    

            blue = set_lsb(blue,message_length_binary[Bits_encoded])
             
            Bits_encoded += 1
            
        #ensures no bit is overridden twice in the transition form encoding the lenth to encoding the message by skippin to next pixel
        if Bits_encoded == binary_length_max_bytes and continue_counter == 1:
            
            pixels[x, y] = (red, green, blue, alpha)
            testbool = True
            continue
        
       

        
        #code does these operations only if entire message has not been encoded and not before the length of the massage have been encoded
        if Bits_encoded < len(message_binary)+binary_length_max_bytes and testbool == True:
            

            red = set_lsb(red,(message_binary[Bits_encoded-binary_length_max_bytes]))#encodes red channel for current pixel 
            Bits_encoded += 1
            
        if Bits_encoded < len(message_binary)+binary_length_max_bytes and testbool == True:
            green = set_lsb(green,(message_binary[Bits_encoded-binary_length_max_bytes]))#encodes green channel for current pixel 
            Bits_encoded += 1
           

        if Bits_encoded < len(message_binary)+binary_length_max_bytes and testbool == True:
            blue = set_lsb(blue,(message_binary[Bits_encoded-binary_length_max_bytes]))#encodes blue channel for current pixel 
            Bits_encoded += 1
            

        pixels[x, y] = (red, green, blue, alpha)
      
  
    return image