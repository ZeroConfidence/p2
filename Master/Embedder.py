from PIL import Image

def set_lsb(n, bit):
   
    if bit == '1':
        return (n | 1)
    else:
        return (n & ~1)


def Carrier_embedder(Carrier,Message):
    image = Image.open(Carrier)

    message_binary = ''.join(format(ord(c),'08b')for c in Message)
    
    message_length_binary = bin(len(Message))[2:]
    message_length_binary = '{:0>16}'.format(message_length_binary)

    pixels = image.load()
    Bits_encoded = 0

    for i in range(image.size[0]):
        for k in range(image.size[1]):
            red, green, blue = pixels[i, k]

            while Bits_encoded < 16:
                

                red = set_lsb(red,message_length_binary[Bits_encoded]) 
                Bits_encoded += 1

                if Bits_encoded==16:
                    break

                green = set_lsb(green,message_length_binary[Bits_encoded]) 
                Bits_encoded += 1

                blue = set_lsb(blue,message_length_binary[Bits_encoded]) 
                Bits_encoded += 1

            if Bits_encoded < len(message_binary+16) & Bits_encoded > 16:
                red = set_lsb(red,(message_binary[Bits_encoded-16]))
                Bits_encoded += 1
            if Bits_encoded < len(message_binary+16) & Bits_encoded > 16:
                green = set_lsb(green,(message_binary[Bits_encoded-16]))
                Bits_encoded += 1
            if Bits_encoded < len(message_binary+16) & Bits_encoded > 16:
                blue = set_lsb(blue,(message_binary[Bits_encoded-16]))
                Bits_encoded += 1

            pixels[i, k] = (red, green, blue)


            if Bits_encoded >= len(message_binary+16) & Bits_encoded > 16:
                return image