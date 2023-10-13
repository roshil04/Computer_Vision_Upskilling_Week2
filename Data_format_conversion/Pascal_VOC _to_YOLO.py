# Function to convert Pascal VOC bounding box to YOLO format
def pascal_voc_to_yolo(x1, y1, x2, y2, image_w, image_h):
    center_x = (x1 + x2) / (2.0 * image_w)
    center_y = (y1 + y2) / (2.0 * image_h)
    width = (x2 - x1) / image_w
    height = (y2 - y1) / image_h
    return [center_x, center_y, width, height]

# Example usage
x1, y1, x2, y2 = 100, 50, 200, 150  # Pascal VOC bounding box coordinates
image_width, image_height = 800, 600  # Image dimensions

yolo_bbox = pascal_voc_to_yolo(x1, y1, x2, y2, image_width, image_height)
print(yolo_bbox)  

# Output: [0.1875, 0.225, 0.125, 0.16666666666666666]
