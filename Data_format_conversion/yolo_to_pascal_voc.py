def yolo_to_pascal_voc(x_center, y_center, w, h, image_w, image_h):
    w = w * image_w
    h = h * image_h
    x1 = ((2 * x_center * image_w) - w) / 2
    y1 = ((2 * y_center * image_h) - h) / 2
    x2 = x1 + w
    y2 = y1 + h
    return [x1, y1, x2, y2]

# Example usage
x_center, y_center, width, height = 0.5, 0.5, 0.4, 0.3  # YOLO bounding box coordinates
image_width, image_height = 800, 600  # Image dimensions

pascal_voc_bbox = yolo_to_pascal_voc(x_center, y_center, width, height, image_width, image_height)
print(pascal_voc_bbox)  

# Output: [240.0, 210.0, 560.0, 390.0]
