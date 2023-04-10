from PIL import Image

def set_lsb(n, bit):
   
    if bit == '1':
        return (n | 1)
    else:
        return (n & ~1)


def Carrier_embedder(Carrier,Message):
    image = Image.open(Carrier)

    message_binary = ''.join(format(ord(c),'08b')for c in Message)

    pixels = image.load()
    pixel_count = 0
    for i in range(image.size[0]):
        for k in range(image.size[1]):

            red, green, blue = pixels[i, k]

            if pixel_count < len(message_binary):
                red = set_lsb(red,(message_binary[pixel_count]))
                pixel_count += 1
            if pixel_count < len(message_binary):
                green = set_lsb(green,(message_binary[pixel_count]))
                pixel_count += 1
            if pixel_count < len(message_binary):
                blue = set_lsb(blue,(message_binary[pixel_count]))
                pixel_count += 1

            pixels[i, k] = (red, green, blue)


            if pixel_count >= len(message_binary):
                return image