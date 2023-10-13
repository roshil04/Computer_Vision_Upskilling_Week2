def yolo_to_coco(x_center, y_center, w, h, image_w, image_h):
    w = w * image_w
    h = h * image_h
    x1 = ((2 * x_center * image_w) - w) / 2
    y1 = ((2 * y_center * image_h) - h) / 2
    return [x1, y1, w, h]

# Example usage
x_center, y_center, width, height = 0.5, 0.5, 0.4, 0.3  # YOLO bounding box coordinates
image_width, image_height = 800, 600  # Image dimensions

coco_bbox = yolo_to_coco(x_center, y_center, width, height, image_width, image_height)
print(coco_bbox)  

# Output: [240.0, 210.0, 320.0, 180.0]
