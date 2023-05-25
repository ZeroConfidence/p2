from PIL import Image
import random
import math
"""
This code is designed to take an image with an encoded message hidden inside
Then extract the message hidden inside an return it to the master code
"""
def read_lsb(n): #Read lsb takes the smallest bit and returns if it is a 0 or 1
    return n & 1 #does binary and operation on the given color value and 1

def Carrier_decoder(Encrypted_image,key):
    image = Encrypted_image#Image.open(Encrypted_image)

    
    pixels = image.load()
    Bits_extracted = 0 #Used to keep track of where in the image the code is currently operating
    binary_message = [] #Used to keep the hidden message in its binary form
    max_bytes = ((image.size[0] * image.size[1] * 3)/8) #finds the maximum number of encoded bytes
    binary_length_max_bytes = math.ceil(math.log2(max_bytes)) #finds the length of the binary prepresentation of max_bytes
    message_length = 0
    
    random.seed(key)# sets key as the seed for the psudo-random number generator 
    Pixel_Coordinates = [(x,y)for x in range(image.size[0]) for y in range(image.size[1])] #loads the coordinates for he pixels into the pixel_coordinate variable 
    random.shuffle(Pixel_Coordinates) #shuffles around the x and y cordinates for pixel_coordinates to make a new psudorandom sequence based on the given key
    message_length_bits=""
    message_bits = ""
    famousbool = False # used for skipping to next pixel after reading length of message
    for x,y in Pixel_Coordinates: 
        red, green, blue,alpha = pixels[x,y]
        continue_counter= 0
        #Checks for the first bits to see how long the encoded message is, the number of bits checked is decided by binary_length_max_bytes 
        if Bits_extracted < binary_length_max_bytes:
            continue_counter =1
            
            message_length_bits = message_length_bits + str(read_lsb(red))#reads from red channel
            
            Bits_extracted += 1
            

        if Bits_extracted < binary_length_max_bytes:    
            message_length_bits = message_length_bits + str(read_lsb(green))#reads from green channel
            
            Bits_extracted += 1
            

        if Bits_extracted < binary_length_max_bytes:    
            message_length_bits = message_length_bits + str(read_lsb(blue))#reads from blue channel
            
            Bits_extracted += 1
            
           
               
        #if statment ensures no bit is read twice after message length is decoded by skiping to next pixel before decoing message
        if Bits_extracted == binary_length_max_bytes and continue_counter == 1:
          
            message_length = int(message_length_bits,2)*8
            famousbool = True
            continue

        
        
        #extracts message from color channels
        if Bits_extracted < message_length+binary_length_max_bytes and famousbool == True:
            red_bit = read_lsb(red)    #reads from red channel
            message_bits = message_bits + str(red_bit)
            Bits_extracted +=1


        if Bits_extracted < message_length+binary_length_max_bytes and famousbool == True:
            green_bit = read_lsb(green)#reads from green channel
            message_bits = message_bits + str(green_bit)
            Bits_extracted +=1


        if Bits_extracted < message_length+binary_length_max_bytes and famousbool == True:
            blue_bit = read_lsb(blue)  #reads from blue channel
            message_bits = message_bits + str(blue_bit)
            Bits_extracted +=1



            #Takes the binary message, splits it into 8 bit chunks, converts the binary chunks to int, converts the int to chr, then joins the chr to a string
    Hidden_message = ''.join([chr(int(''.join(message_bits[i:i+8]),2))for i in range(0,len(message_bits),8)])
              

    return Hidden_message
