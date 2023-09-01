from data import *


# Function that reads an image file and returns Header object and pixels list.
# Return a tuple containing the Header object and the pixels list.

def read_file(fname: str) -> (Header, list[str]):
    try:
        fin = open(fname)
    except:
        print("cannot open")
        exit()
    fin.readline()
    wh = fin.readline().strip().split()
    header = Header(int(wh[0]), int(wh[1]), int(fin.readline()))
    pixels = []
    for line in fin:
        pixels.extend(map(int, line.strip().split()))
    return header, pixels


# Function that take pixels list and return list of Pixel objects in groups of 3

def pixel_objects(lst: list[str]) -> list[Pixel]:
    pixels = []
    for i in range(0, len(lst), 3):
        red = int(lst[i])
        green = int(lst[i + 1])
        blue = int(lst[i + 2])
        pixels.append(Pixel(red, green, blue))
    return pixels


# Create iamge when given header, list of pixels and file name

def create_image(header: Header, pixels: list[Pixel], output_file: str):
    fout = open(output_file, 'w')
    fout.write("P3\n")
    fout.write('{} {}\n'.format(header.width, header.height))
    fout.write('{}\n'.format(header.max_color))
    for pixel in pixels:
        fout.write('{} {} {}\n'.format(pixel.red, pixel.green, pixel.blue))
    fout.close()

# negate: inverts the image by subtracting each pixel's color value from 255, ensuring the result is non-negative, and then adds it to a new list

def negate(pixels: list[Pixel]) -> list[Pixel]:
    negated_pixels = []
    for pixel in pixels:
        red = (255 - pixel.red)
        green = (255 - pixel.green)
        blue = (255 - pixel.blue)
        negated_pixel = Pixel(red, green, blue)
        negated_pixels.append(negated_pixel)
    return negated_pixels


# high_contrast: enhances image contrast. If the value is greater than 127, set it to 255, otherwise set it to 0

def high_contrast(pixels: list[Pixel]) -> list[Pixel]:
    contrasted_pixels = []
    for pixel in pixels:
        if pixel.red > 127:
            red = 255
        else:
            red = 0
        if pixel.green > 127:
            green = 255
        else:
            green = 0
        if pixel.blue > 127:
            blue = 255
        else:
            blue = 0
        contrasted_pixel = Pixel(red, green, blue)
        contrasted_pixels.append(contrasted_pixel)
    return contrasted_pixels


# gray_scale: take the average of RGB values and set as the new RGB values 

def gray_scale(pixels: list[Pixel]) -> list[Pixel]:
    gray_pixels = []
    for pixel in pixels:
        avg = (pixel.red + pixel.green + pixel.blue) / 3
        red = avg
        green = avg
        blue = avg
        gray_pixel = Pixel(red, green, blue)
        gray_pixels.append(gray_pixel)
    return gray_pixels


# remove_color: function removes the color the user inputs from a particular image

def remove_color(pixels: list[Pixel], color: str) -> list[Pixel]:
    removed_pixels = []
    for pixel in pixels:
        if color == 'red':
            pixel.red = 0
        if color == 'green':
            pixel.blue = 0
        if color == 'blue':
            pixel.green = 0
        removed_pixels.append(Pixel(pixel.red, pixel.green, pixel.blue))
    return removed_pixels


