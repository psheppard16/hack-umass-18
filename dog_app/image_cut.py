from PIL import Image, ImageFilter

image = Image.open('Dog_on_grass.jpg')
image = image.filter(ImageFilter.FIND_EDGES)
image.save('Dog_on_grass_new.jpg')