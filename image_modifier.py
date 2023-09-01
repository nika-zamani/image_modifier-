from data import *


# Write a function that reads an image file and returns Header object and pixels list.
# def read_file(fname: str) -> (Header, list[str]):
# Open the file with the given filename using the open() function and assign it to a variable fin.
# Read the first line of the file using the readline() method of the fin object to skip the first line.
# Read the second line of the file using the readline() method of the fin object and split it into a list of strings
# using the split() method. Assign the first and second elements of the list to variables width and height respectively,
# and convert them to integers using the int() function.
# Read the third line of the file using the readline() method of the fin object and convert it to an integer using the
# int() function. Assign it to a variable max_color.
# Create a new Header object using the width, height, and max_color variables.
# Create an empty list pixels.
# Loop over the remaining lines of the file using a for loop that iterates over the fin object.
# Strip the line of any whitespace using the strip() method and split it into a list of strings using the split() method.
# Convert each string in the list to an integer using the map() function and the int() function. Use the extend() method
# of the pixels list to add the resulting list of integers to the pixels list.
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


# Write a function that take pixels list and return list of Pixel objects in groups of 3
# def pixel_objects(lst: list[str]) -> list[Pixel]:
# Initialize an empty list called pixels to hold the resulting Pixel objects.
# Loop through the input list lst with a step of 3.
# Inside the loop, extract the red, green, and blue values from the current 3-item slice of lst.
# Convert the red, green, and blue values from strings to integers using the int() function.
# Create a new Pixel object with the red, green, and blue values, and append it to the pixels list.
# After the loop completes, return the pixels list containing all the Pixel objects.

def pixel_objects(lst: list[str]) -> list[Pixel]:
    pixels = []
    for i in range(0, len(lst), 3):
        red = int(lst[i])
        green = int(lst[i + 1])
        blue = int(lst[i + 2])
        pixels.append(Pixel(red, green, blue))
    return pixels


# create iamge when given header and list of pixels and file name
# def create_image(header: Header, pixels: list[Pixel], output_file: str):
# Open the output file in write mode using open() and assign the file object to a variable
# Write the PPM header to the file using fout.write() by first writing "P3\n", followed by the width and height of the image in pixels, separated by a space and ending with a newline character, and finally the maximum color value allowed for the image (usually 255) followed by a newline character.
# Iterate over each pixel in the pixels list and write its RGB values to the file using fout.write(). The format for each pixel is "R G B\n" where R, G, and B are the red, green, and blue components of the pixel, respectively.
# Close the file using fout.close().

def create_image(header: Header, pixels: list[Pixel], output_file: str):
    fout = open(output_file, 'w')
    fout.write("P3\n")
    fout.write('{} {}\n'.format(header.width, header.height))
    fout.write('{}\n'.format(header.max_color))
    for pixel in pixels:
        fout.write('{} {} {}\n'.format(pixel.red, pixel.green, pixel.blue))
    fout.close()


# negate function: takes the list of Pixel objects and subtract each pixel value from 255, take its absolute value and write to the new list.
# def negate(pixels: list[Pixel]) -> list[Pixel]:
# Create an empty list to store the negated pixels.
# For each pixel in the input list:
# Calculate the negated red, green, and blue values.
# Create a new Pixel object with the negated colors.
# Append the new pixel to the negated pixels list.
# Return the negated pixels list.

def negate(pixels: list[Pixel]) -> list[Pixel]:
    negated_pixels = []
    for pixel in pixels:
        red = (255 - pixel.red)
        green = (255 - pixel.green)
        blue = (255 - pixel.blue)
        negated_pixel = Pixel(red, green, blue)
        negated_pixels.append(negated_pixel)
    return negated_pixels


# Take the list of Pixel objects and apply high contrast to each pixel. If the value is greater than 127, set it to 255, otherwise set it to 0
# def high_contrast(pixels: list[Pixel]) -> list[Pixel]:
# Create an empty list to store the high-contrasted pixels.
# For each pixel in the input list:
# If the red value of the pixel is greater than 127, set the red value of the contrasted pixel to 255, else set it to 0.
# If the green value of the pixel is greater than 127, set the green value of the contrasted pixel to 255, else set it to 0.
# If the blue value of the pixel is greater than 127, set the blue value of the contrasted pixel to 255, else set it to 0.
# Create a new Pixel object with the high-contrasted colors.
# Append the new pixel to the high-contrasted pixels list.
# Return the high-contrasted pixels list.

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


# take the RGB value and convert the values to average of original RGB value
# def gray_scale(pixels: list[Pixel]) -> list[Pixel]:
# Create an empty list to store the grayscale pixels.
# For each pixel in the input list:
# Calculate the average of the red, green, and blue values of the pixel.
# Set the red, green, and blue values of the grayscale pixel to the average value.
# Create a new Pixel object with the grayscale colors.
# Append the new pixel to the grayscale pixels list.
# Return the grayscale pixels list.

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


# function removes the color that the user inputs from a particular image
# def remove_color(pixels: list[Pixel], color: str) -> list[Pixel]:
# Create an empty list to store the removed color pixels.
# For each pixel in the input list:
# Check the color argument to determine which color to remove.
# Set the value of the corresponding color in the pixel to 0.
# Create a new Pixel object with the modified colors.
# Append the new pixel to the removed color pixels list.
# Return the removed color pixels list.

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


