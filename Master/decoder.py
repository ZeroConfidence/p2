from PIL import Image

def read_lsb(n):
    return n & 1

def Carrier_decoder(Encrypted_image):
    image = Image.open(Encrypted_image)

    bits = image.load()

    pixel_count = 0
    for i in range(image.size[0]):
        for k in range(image.size[1]):
            red, green, blue = bits[i, k]

            while pixel_count < 8:
                binary_length = [0]*8
                binary_length[pixel_count] = read_lsb(red) 
                pixel_count += 1

                binary_length[pixel_count] = read_lsb(red) 
                pixel_count += 1

                if pixel_count==8:
                    message_length = int(''.join(map(str, binary_length)),2)
                    break

                binary_length[pixel_count] = read_lsb(red) 
                pixel_count += 1

            if pixel_count < message_length+8:
                red = read_lsb(red)
                pixel_count += 1
            if pixel_count < message_length+8:
                green = read_lsb(green)
                pixel_count += 1
            if pixel_count < message_length+8:
                blue = read_lsb(blue)
                pixel_count += 1