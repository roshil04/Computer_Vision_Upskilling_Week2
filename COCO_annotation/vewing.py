import json
import os
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt

# Load the COCO annotation JSON file
with open("coco_annotations.json", "r") as json_file:
    coco_annotations = json.load(json_file)

# Load the original image
image_path = "C:\\Users\\Roshil\\Downloads\\Week2\\cat_dog.jpg"
original_image = Image.open(image_path)

# Create a list to store annotated images
annotated_images = []

# Loop through bounding box annotations to create annotated images
for annotation in coco_annotations["annotations"]:
    category_id = annotation["category_id"]
    bbox = annotation["bbox"]
    
    # Create a copy of the original image
    annotated_image = original_image.copy()
    
    # Create a drawing context
    draw = ImageDraw.Draw(annotated_image)
    
    # Draw a rectangle (bounding box) on the annotated image
    draw.rectangle([(bbox[0], bbox[1]), (bbox[0] + bbox[2], bbox[1] + bbox[3])], outline="red", width=3)
    
    # Save the annotated image with a unique filename
    annotated_image_filename = f"annotated_image_{category_id}.jpg"
    annotated_image.save(annotated_image_filename)

    # Visualize the annotated image with bounding boxes
    annotated_images.append(annotated_image)

# Display all annotated images in one row
fig, axes = plt.subplots(1, len(annotated_images), figsize=(15, 5))
for i, img in enumerate(annotated_images):
    axes[i].imshow(img)
    axes[i].axis('off')

plt.tight_layout()
plt.show()

print(f"Annotated images with bounding boxes saved to the current directory")
