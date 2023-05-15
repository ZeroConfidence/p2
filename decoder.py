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
    image = Encrypted_image#Image.open(Encrypted_image)

    
    pixels = image.load()
    Bits_extracted = 0 #Used to keep track of where in the image the code is currently operating
    binary_message = [] #Used to keep the hidden message in its binary form
    max_bytes = ((image.size[0] * image.size[1] * 3)/8) #finds the maximum number of encoded bytes
    binary_length_max_bytes = math.ceil(math.log2(max_bytes)) #finds the length of the binary prepresentation of max_bytes
    
    print("max",max_bytes,"bin_len_max bytes",binary_length_max_bytes)
    random.seed(key)# sets key as the seed for the psudo-random number generator 
    Pixel_Coordinates = [(x,y)for x in range(image.size[0]) for y in range(image.size[1])] #loads the coordinates for he pixels into the pixel_coordinate variable 
    random.shuffle(Pixel_Coordinates) #shuffles around the x and y cordinates for pixel_coordinates to make a new psudorandom sequence based on the given key
    message_length_bits=""
    for x,y in Pixel_Coordinates:
        red, green, blue,alpha = pixels[x,y]
        
        #Checks for the first bits to see how long the encoded message is, the number of bits checked is decided by max_bytes 
        if Bits_extracted < binary_length_max_bytes:
            print("cords",x,y)
            print("red",red)
            print("green",green)
            print("blue",blue)
            message_length_bits = message_length_bits + str(read_lsb(red))
            print("red-read",read_lsb(red))
            print(message_length_bits)
            Bits_extracted += 1
            print ("bitNR",Bits_extracted)

        if Bits_extracted < binary_length_max_bytes:    
            message_length_bits = message_length_bits + str(read_lsb(green))
            print("green-read",read_lsb(green))
            print(message_length_bits)
            Bits_extracted += 1
            print ("bitNR",Bits_extracted)

        if Bits_extracted < binary_length_max_bytes:    
            message_length_bits = message_length_bits + str(read_lsb(blue))
            print("blue-read",read_lsb(blue))
            print(message_length_bits)
            Bits_extracted += 1
            print ("bitNR",Bits_extracted)
            
    print("message_length_bits",message_length_bits)       
        
        
            
          
    message_length = int(message_length_bits,2)*8            
    print("msg len",message_length)
    message_bits = []
    Bits_extracted = 0
    for x,y in Pixel_Coordinates:
        if  Bits_extracted<binary_length_max_bytes:  
            if x == 0 and y == 0:
                continue
            if len(message_bits) >= message_length:
                break
            
            red,green,blue,alpha = image.getpixel((x,y))
            if  Bits_extracted<binary_length_max_bytes: 
                red_bit = read_lsb(red)
                message_bits.extend([red_bit,green_bit,blue_bit])
            Bits_extracted += 1
            if  Bits_extracted<binary_length_max_bytes:     
                green_bit = read_lsb(green)
            Bits_extracted += 1
            if  Bits_extracted<binary_length_max_bytes:     
                blue_bit = read_lsb(blue)
            Bits_extracted += 1
            
        
        #Code does these operations only if entire message has not been read, after the first 16 bits already have been read
        
                
        #Code extracts the hidden_message once the entire message has been read and returns it in text form
    print("messagebits",message_bits)
    #print("message lengyh",message_length)
    #print("len",len(message_bits))
            #Takes the binary message, splits it into 8 bit chunks, converts the binary chunks to int, converts the int to chr, then joins the chr to a string
    Hidden_message = ''.join([chr(int(''.join(message_bits[i:i+8]),2))for i in range(0,len(message_bits),8)])
            #Hidden_message = Hidden_message.replace('\x00','') + chr('a')
    print(Hidden_message)  

    return Hidden_message #f"redpixelvalue:{red}(binary:{bin(red)})"
