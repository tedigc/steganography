from PIL import Image
from numpy import array

# Check if two arrays are the same width and height
def same_dimensions(array1, array2):
    same_width = len(array1[0]) == len(array2[0])
    same_height = len(array1) == len(array2)
    return same_width and same_height

# Encode one image into another
def encode(array1, array2):
    if not same_dimensions(array1, array2):
        print("Images not same length")
        return false

    for j in range(0, len(array1)):
        for i in range(0, len(array1[0])):
            newVal = (array1[j, i, 2] >> 1 << 1) | array2[j, i]
            array1[j, i, 2] = newVal

    return Image.fromarray(array1, 'RGB')

# Decode the encoded monochrome image
def decode(image):
    image_data = array(image)
    width = len(image_data[0])
    height = len(image_data)
    
    for y in range(0, height):
        for x in range(0, width):
            format_bin = format(image_data[y, x, 2], '08b')
            bit = (int(format_bin) % 2)
            image_data[y, x, 0] = 255 * (1-bit)
            image_data[y, x, 1] = 255 * (1-bit)
            image_data[y, x, 2] = 255 * (1-bit)

    return Image.fromarray(image_data, 'RGB')

image1 = Image.open("images/duck.jpg")
image2 = Image.open("images/penguin.png")

array1 = array(image1)
array2 = array(image2)

encoded = encode(array1, array2)
encoded.show()

decoded = decode(encoded)
decoded.show()
