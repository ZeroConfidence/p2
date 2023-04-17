from PIL import Image

def Carrier_decoder(Carrier_ec):
    image = Image.open(Carrier_ec)

bits = image.load()

pixel_count = 0
for i in range(image.size[0]):
    for k in range(image.size[1]):

        red, green, blue = bits[i, k]

        if pixel_count < len():
            red = set_lsb(red,([pixel_count]))
            pixel_count += 1
        if pixel_count < len():
            green = set_lsb(green,([pixel_count]))
            pixel_count += 1
        if pixel_count < len():
            blue = set_lsb(blue,([pixel_count]))
            pixel_count += 1
