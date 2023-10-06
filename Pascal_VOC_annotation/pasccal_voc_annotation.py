import os
import xml.etree.ElementTree as ET

# Define the image and annotation information
image_path = 'C:/Users/Roshil/Downloads/Week2/cat_dog.jpg'  # Path to the image
output_folder = 'C:/Users/Roshil/Downloads/Week2'  # Folder to save the XML file
output_filename = 'cat_dog.xml'  # XML filename

# Defining the object information
objects = [
    {
        'name': 'cat',
        'xmin': 160,
        'ymin': 360,
        'xmax': 20,
        'ymax': 150
    },
    {
        'name': 'dog',
        'xmin': 450,
        'ymin': 50,
        'xmax': 150,
        'ymax': 450
    }
]

# Creating the XML structure
annotation = ET.Element("annotation")
ET.SubElement(annotation, "folder").text = os.path.dirname(image_path)
ET.SubElement(annotation, "filename").text = os.path.basename(image_path)
ET.SubElement(annotation, "path").text = image_path

size = ET.SubElement(annotation, "size")
ET.SubElement(size, "width").text = str(800)  # Image width
ET.SubElement(size, "height").text = str(600)  # Image height
ET.SubElement(size, "depth").text = str(3)  # Assuming RGB image

# Iterate over objects and add them to the XML
for obj_info in objects:
    object_elem = ET.SubElement(annotation, "object")
    ET.SubElement(object_elem, "name").text = obj_info['name']
    
    bndbox = ET.SubElement(object_elem, "bndbox")
    ET.SubElement(bndbox, "xmin").text = str(obj_info['xmin'])
    ET.SubElement(bndbox, "ymin").text = str(obj_info['ymin'])
    ET.SubElement(bndbox, "xmax").text = str(obj_info['xmax'])
    ET.SubElement(bndbox, "ymax").text = str(obj_info['ymax'])

# Creating a prettified XML string
xml_str = ET.tostring(annotation, encoding='unicode')
xml_str = xml_str.replace("  ", "\t")  # Indentation for prettifying

# Saving the XML to a file in the specified output folder
xml_file_path = os.path.join(output_folder, output_filename)
with open(xml_file_path, "w") as xml_file:
    xml_file.write(xml_str)

print(f"XML file saved at: {xml_file_path}")
