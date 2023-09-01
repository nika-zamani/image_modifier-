from image_modifier import *
from image_modifier import create_image


def main():
    input_file = input('Enter input file name:')

    output_file = input('Enter output file name:')

    command = input('command: "negate", "high contrast", "gray scale", "remove <color>" where <color> is "red", "green", or "blue" or “shrink” ')

    # read the input file and get its header and pixels
    header, pixels_lst = read_file(input_file)

    # convert the pixels list to a list of Pixel objects
    pixels = pixel_objects(pixels_lst)

    if command == "negate":
        print("image created")
        modified_image = negate(pixels)
        create_image(header, modified_image, output_file)
        exit()
    if command == "high contrast":
        print("image created")
        modified_image = high_contrast(pixels)
        create_image(header, modified_image, output_file)
        exit()
    if command == "gray scale":
        print("image created")
        modified_image = gray_scale(pixels)
        create_image(header, modified_image, output_file)
        exit()
    if command[:7] == "remove ":
        color = command[7:]
        if color == "red" or color == "green" or color == "blue":
            print("image created")
            modified_image = remove_color(pixels, color)
            create_image(header, modified_image, output_file)
            exit()
        else:
            print("Invalid color")
    else:
        print("Invalid command")


if __name__ == '__main__':
    main()
