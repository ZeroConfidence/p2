from PIL import Image
"""
This code is designed to take an image with an encoded message hidden inside
Then extract the message hidden inside an return it to the master code
"""
def read_lsb(n): #Read lsb takes the smallest bit and returns if it is a 0 or 1
    return n & 1

def Carrier_decoder(Encrypted_image):
    image = Image.open(Encrypted_image)

    pixels = image.load()

    Bits_extracted = 0 #Used to keep track of where in the image the code is currently operating
    binary_message = [] #Used to keep the hidden message in its binary form

    
    #for loops used to keep the operations inside the image boundries
    for i in range(image.size[0]):
        for k in range(image.size[1]):
            red, green, blue = pixels[i, k] #Saves the pixel location for each color

            #Checks for the first 16 bits to see how long the encoded message is
            while Bits_extracted < 16:
                binary_length = [0]*16

                binary_length[Bits_extracted] = read_lsb(red) 
                Bits_extracted += 1

                if Bits_extracted==16:
                    message_length = int(''.join(map(str, binary_length)),2) #Converts the 16 binary string to int
                    break

                binary_length[Bits_extracted] = read_lsb(green) 
                Bits_extracted += 1

                binary_length[Bits_extracted] = read_lsb(blue) 
                Bits_extracted += 1

            #Code does these operations only if entire message has not been read, after the first 16 bits already have been read
            if Bits_extracted < (message_length*8)+16 & Bits_extracted>16:
                binary_message.append(read_lsb(red))
                Bits_extracted += 1

            if Bits_extracted < (message_length*8)+16 & Bits_extracted>16:
                binary_message.append(read_lsb(green))
                Bits_extracted += 1

            if Bits_extracted < (message_length*8)+16 & Bits_extracted>16:
                binary_message.append(read_lsb(blue))
                Bits_extracted += 1
                
            #Code extracts the hidden_message once the entire message has been read and returns it in text form
            if Bits_extracted == (message_length*8)+16:
                #Takes the binary message, splits it into 8 bit chunks, converts the binary chunks to int, converts the int to chr, then joins the chr to a string
                Hidden_message = ''.join([chr(int(''.join(binary_message[i:i+8]),2))for i in range(0,len(binary_message),8)])
                return Hidden_message
