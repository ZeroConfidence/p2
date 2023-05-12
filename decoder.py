from PIL import Image
import random
import math
"""
This code is designed to take an image with an encoded message hidden inside
Then extract the message hidden inside an return it to the master code
"""
def read_lsb(n): #Read lsb takes the smallest bit and returns if it is a 0 or 1
    return n & 1

def Carrier_decoder(Encrypted_image,key):
    image = Image.open(Encrypted_image)

    pixels = image.load()

    Bits_extracted = 0 #Used to keep track of where in the image the code is currently operating
    binary_message = [] #Used to keep the hidden message in its binary form
    max_bytes = ((image.size[0] * image.size[1] * 3) / 8) #finds the maximum number of encoded bytes
    binary_length_max_bytes = math.ceil(math.log2(max_bytes)) #finds the length of the binary prepresentation of max_bytes

    
    random.seed(key)# sets key as the seed for the psudo-random number generator 
    Pixel_Coordinates = [(x,y)for x in range(image.size[0]) for y in range(image.size[1])] #loads the coordinates for he pixels into the pixel_coordinate variable 
    random.shuffle(Pixel_Coordinates) #shuffles around the x and y cordinates for pixel_coordinates to make a new psudorandom sequence based on the given key
    
    for x,y in Pixel_Coordinates:
        red, green, blue = pixels[x, y]

        #Checks for the first bits to see how long the encoded message is, the number of bits checked is decided by max_bytes 
        while Bits_extracted < binary_length_max_bytes:
            binary_length = [0]*binary_length_max_bytes

            binary_length[Bits_extracted] = read_lsb(red) 
            Bits_extracted += 1

            if Bits_extracted==binary_length_max_bytes:
                message_length = int(''.join(map(str, binary_length)),2) #Converts the 16 binary string to int
                break

            binary_length[Bits_extracted] = read_lsb(green) 
            Bits_extracted += 1

            binary_length[Bits_extracted] = read_lsb(blue) 
            Bits_extracted += 1

        #Code does these operations only if entire message has not been read, after the first 16 bits already have been read
        if Bits_extracted < (message_length*8)+binary_length_max_bytes & Bits_extracted>binary_length_max_bytes:
            binary_message.append(read_lsb(red))
            Bits_extracted += 1

        if Bits_extracted < (message_length*8)+binary_length_max_bytes & Bits_extracted>binary_length_max_bytes:
            binary_message.append(read_lsb(green))
            Bits_extracted += 1

        if Bits_extracted < (message_length*8)+binary_length_max_bytes & Bits_extracted>binary_length_max_bytes:
            binary_message.append(read_lsb(blue))
            Bits_extracted += 1
                
        #Code extracts the hidden_message once the entire message has been read and returns it in text form
        if Bits_extracted == (message_length*8)+binary_length_max_bytes:
            #Takes the binary message, splits it into 8 bit chunks, converts the binary chunks to int, converts the int to chr, then joins the chr to a string
            Hidden_message = ''.join([chr(int(''.join(binary_message[i:i+8]),2))for i in range(0,len(binary_message),8)])
            #Hidden_message = Hidden_message.replace('\x00','') + chr('a')
            return Hidden_message
