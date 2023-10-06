from PIL import Image
from PIL import ImageDraw
import xml.etree.ElementTree as ET

# Path to the annotated image
image_path = 'C:/Users/Roshil/Downloads/Week2/cat_dog.jpg'

# Loading the image
image = Image.open(image_path)

# Creating a drawing context
draw = ImageDraw.Draw(image)

# Path to the annotated XML file
xml_file_path = 'C:/Users/Roshil/Downloads/Week2/cat_dog.xml'  # Update with your XML file path

# Parse the XML annotation file
tree = ET.parse(xml_file_path)
root = tree.getroot()

# Defining colors for drawing bounding boxes and labels
box_color = (0, 255, 0)  # Green color (R, G, B)
label_color = (255, 255, 255)  # White color (R, G, B)

# Iterate through object elements and draw bounding boxes and labels
for obj in root.findall('object'):
    class_name = obj.find('name').text
    bbox = obj.find('bndbox')
    xmin = int(bbox.find('xmin').text)
    ymin = int(bbox.find('ymin').text)
    xmax = int(bbox.find('xmax').text)
    ymax = int(bbox.find('ymax').text)

    # Drawing the bounding box
    draw.rectangle([xmin, ymin, xmax, ymax], outline=box_color)

    # Calculate label position
    label_x = xmin
    label_y = ymin - 15  # Adjust for label position above the bounding box

    # Drawing the label
    draw.text((label_x, label_y), class_name, fill=label_color)

# Showing the annotated image
image.show()
