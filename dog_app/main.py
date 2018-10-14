import io

def main(path):
    """Localize objects in the local image.

    Args:
    path: The path to the local file.
    """
    from google.cloud import vision
    from PIL import Image
    client = vision.ImageAnnotatorClient()

    with open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)
    img = Image.open(path)

    objects = client.object_localization(
        image=image).localized_object_annotations

    print('Number of objects found: {}'.format(len(objects)))
    for object_ in objects:
        if object_.name == "Dog":
            print(object_.bounding_poly.normalized_vertices[0].x)
            area = (object_.bounding_poly.normalized_vertices[0].x, object_.bounding_poly.normalized_vertices[0].y, object_.bounding_poly.normalized_vertices[2].x, object_.bounding_poly.normalized_vertices[2].y)
            crop_img = img.crop(area)
            out = io.BytesIO()
            crop_img.save(out, format='JPEG')
            hex_data = out.getvalue()
            content_ = hex_data.read()
            crop_img_ = vision.types.Image(content = content_)
            response = client.image_properties(image=crop_img_)
            props = response.image_properties_annotation
            print('Properties:')
            total = 0

            for color in props.dominant_colors.colors:
                total += color.pixel_fraction
                print('fraction: {}'.format(color.pixel_fraction))
                print('\tr: {}'.format(color.color.red))
                print('\tg: {}'.format(color.color.green))
                print('\tb: {}'.format(color.color.blue))
                print('\ta: {}'.format(color.color.alpha))
            print("\nThis is total: {}\n".format(total))


            # print('\n{} (confidence: {})'.format(object_.name, object_.score))
            # print('Normalized bounding polygon vertices: ')
            # for vertex in object_.bounding_poly.normalized_vertices:
            #     print(' - ({}, {})'.format(vertex.x, vertex.y))

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
    total = 0

    for color in props.dominant_colors.colors:
        total += color.pixel_fraction
        print('fraction: {}'.format(color.pixel_fraction))
        print('\tr: {}'.format(color.color.red))
        print('\tg: {}'.format(color.color.green))
        print('\tb: {}'.format(color.color.blue))
        print('\ta: {}'.format(color.color.alpha))
    print("\nThis is total: {}\n".format(total))



main("Doggo.jpg")