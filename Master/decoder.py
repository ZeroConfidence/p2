from PIL import Image

def read_lsb(n):
    return n & 1

def Carrier_decoder(Encrypted_image):
    image = Image.open(Encrypted_image)

    bits = image.load()

    pixel_count = 0
    binary_message = []

    for i in range(image.size[0]):
        for k in range(image.size[1]):
            red, green, blue = bits[i, k]

            while pixel_count < 16:
                binary_length = [0]*16

                binary_length[pixel_count] = read_lsb(red) 
                pixel_count += 1

                if pixel_count==16:
                    message_length = int(''.join(map(str, binary_length)),2)
                    break

                binary_length[pixel_count] = read_lsb(green) 
                pixel_count += 1

                binary_length[pixel_count] = read_lsb(blue) 
                pixel_count += 1

            if pixel_count < (message_length*8)+16:
                binary_message.append(read_lsb(red))
                pixel_count += 1

            if pixel_count < (message_length*8)+16:
                binary_message.append(read_lsb(green))
                pixel_count += 1

            if pixel_count < (message_length*8)+16:
                binary_message.append(read_lsb(blue))
                pixel_count += 1

            if pixel_count == (message_length*8)+16:
                Hidden_message = ''.join([chr(int(''.join(binary_message[i:i+8]),2))for i in range(0,len(binary_message),8)])
                return Hidden_message