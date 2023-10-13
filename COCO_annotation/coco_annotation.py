import json
import os
from PIL import Image

# Creating a dictionary to hold the COCO annotation data
coco_data = {
    "info": {
        "description": "My COCO Dataset",
        "url": "https://example.com",
        "version": "1.0",
        "year": 2023,
        "contributor": "Your Name",
        "date_created": "2023-09-15"
    },
    "licenses": [
        {
            "url": "https://creativecommons.org/licenses/by/4.0/",
            "id": 1,
            "name": "Creative Commons Attribution 4.0 License"
        }
    ],
    "categories": [
        {
            "supercategory": "animals",
            "id": 1,
            "name": "cat"
        },
        {
            "supercategory": "animals",
            "id": 2,
            "name": "dog"
        }
    ],
    "images": [],
    "annotations": []
}

# Defining the directory containing your images
image_dir = "C:\\Users\\Roshil\\Downloads\\Week2\\"
image_file_name = "cat_dog.jpg"

# Generating image and annotation data for the cat
cat_image_id = 1
cat_annotation_id = 1

image = Image.open(os.path.join(image_dir, image_file_name))
image_width, image_height = image.size

# Creating an image entry
image_info = {
    "license": 1,
    "file_name": image_file_name,
    "height": image_height,
    "width": image_width,
    "id": cat_image_id
}

# Creating a cat annotation
cat_annotation_info = {
    "id": cat_annotation_id,
    "image_id": cat_image_id,
    "category_id": 1,  # Cat category ID
    "bbox": [20, 150, 160, 360],  # [x, y, width, height]
    "area": 576000,  # Calculated as width * height
    "iscrowd": 0
}

# Append the image and cat annotation data to the COCO dictionary
coco_data["images"].append(image_info)
coco_data["annotations"].append(cat_annotation_info)

# Generating a dog annotation in the same image
dog_annotation_id = 2

# Creating a dog annotation
dog_annotation_info = {
    "id": dog_annotation_id,
    "image_id": cat_image_id,
    "category_id": 2,  # Dog category ID
    "bbox": [150, 50, 450, 450],  # [x, y, width, height]
    "area": 202500,  # Calculated as width * height
    "iscrowd": 0
}

# Append the dog annotation data to the COCO dictionary
coco_data["annotations"].append(dog_annotation_info)

# Save the COCO annotation data to a JSON file
output_json_file = "coco_annotations.json"
with open(output_json_file, "w") as json_file:
    json.dump(coco_data, json_file)

print(f"COCO annotations saved to {output_json_file}")

# Loading and print the generated COCO annotations
with open(output_json_file, "r") as json_file:
    coco_annotations = json.load(json_file)

# Printing the JSON data
print(json.dumps(coco_annotations, indent=4))
