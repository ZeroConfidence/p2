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

    pixels = image.load()
    pixel_count = 0

    for i in range(image.size[0]):
        for k in range(image.size[1]):
            red, green, blue = pixels[i, k]

            while pixel_count < 16:
                

                red = set_lsb(red,message_length_binary[pixel_count]) 
                pixel_count += 1

                if pixel_count==16:
                    break

                green = set_lsb(green,message_length_binary[pixel_count]) 
                pixel_count += 1

                blue = set_lsb(blue,message_length_binary[pixel_count]) 
                pixel_count += 1

            if pixel_count < len(message_binary+16):
                red = set_lsb(red,(message_binary[pixel_count-16]))
                pixel_count += 1
            if pixel_count < len(message_binary+16):
                green = set_lsb(green,(message_binary[pixel_count-16]))
                pixel_count += 1
            if pixel_count < len(message_binary+16):
                blue = set_lsb(blue,(message_binary[pixel_count-16]))
                pixel_count += 1

            pixels[i, k] = (red, green, blue)


            if pixel_count >= len(message_binary+16):
                return image