import io
import os
import webcolors

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.join(
    os.path.dirname(__file__),
    'doggo.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations


# checks if there is a dog in the image
# returns DOGGO if there is a dog in the image and "No :(" if there isn't
def is_doggo(labels):
    print('Labels:')
    for label in labels:
        if label.description == "dog":
            return "DOGGO"
    return "No :("


# this function takes the RGB value given from Google API and gives an approximate color in English
# such as "red", "cyan" or "navy blue"
def get_color_name(requested_color):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_color)
    except ValueError:
        min_colors = {}
        for key, name in webcolors.css3_hex_to_names.items():
            r_c, g_c, b_c = webcolors.hex_to_rgb(key)
            rd = (r_c - requested_color[0]) ** 2
            gd = (g_c - requested_color[1]) ** 2
            bd = (b_c - requested_color[2]) ** 2
            min_colors[(rd + gd + bd)] = name
        closest_name = min_colors[min(min_colors.keys())]
        actual_name = None
    return actual_name, closest_name


# returns the RGB values of the color with the highest fraction, meaning the color that shows up the most in the image
def detect_properties(path):
    """Detects image properties in the file."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.image_properties(image=image)
    props = response.image_properties_annotation
    print('Properties:')
    maxi = -10
    max_red = 0
    max_green = 0
    max_blue = 0
    #all of the values of the fraction should be from 0-1.0
    #setting maximum to 10 guaruntees that the maximum will be found in the array of props.dominant_color.colors

    for color in props.dominant_colors.colors:
        if color.pixel_fraction > maxi:
            maxi = color.pixel_fraction
            max_red = color.color.red
            max_green = color.color.green
            max_blue = color.color.blue
    return max_red, max_green, max_blue
        # print('fraction: {}'.format(color.pixel_fraction))
        # print('\tr: {}'.format(color.color.red))
        # print('\tg: {}'.format(color.color.green))
        # print('\tb: {}'.format(color.color.blue))
        # print('\ta: {}'.format(color.color.alpha))
    #print("\nThis is maximum: {} {} {} {}\n".format(maxi, max_red, max_green, max_blue))


# main function that takes the name of the image and runs all the analysis :) is it a dog? find out!
def run_doggo_detection(path):
    red, green, blue = detect_properties(path)
    requested_color = (red, green, blue)
    actual_name, closest_name = get_color_name(requested_color)

    print("Is your doggo a doggo? {}".format(is_doggo(labels)))
    if actual_name != None:
        print("Actual color name:", actual_name, ", or:", closest_name)
    else:
        print("Color name:", closest_name)

run_doggo_detection("doggo_grass.jpg")