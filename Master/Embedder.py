from PIL import Image


def Carrier_embedder(Carrier,Message):
    image = Image.open(Carrier)

    message_binary = ''.join(format(ord(c),'08b')for c in Message)

    Pixels = image.load()
    pixel_count = 0
    for i in range(image.size[0]):
        for k in range(image.size[1]):

            r, g, b = pixels[i, k]

            if pixel_count < len(message_binary):
                r = set_lsb(r,(message_binary[pixel_count]))
                pixel_count += 1
            if pixel_count < len(message_binary):
                g = set_lsb(g,(message_binary[pixel_count]))
                pixel_count += 1
            if pixel_count < len(message_binary):
                b = set_lsb(b,(message_binary[pixel_count]))
                pixel_count += 1

            Pixels[i, k] = (r, g, b)


            if pixel_count >= len(message_binary):
                return image