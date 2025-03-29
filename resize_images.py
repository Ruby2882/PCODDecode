from PIL import Image
import os

# List of images to resize
images = [
    'static/9.jpg',
    'static/11.jpg',
    'static/10.jpg',
    'static/4.jpg'
]

# New dimensions
new_size = (100, 100)

for image_path in images:
    with Image.open(image_path) as img:
        # Resize image
        img = img.resize(new_size)
        # Save the resized image, overwriting the original
        img.save(image_path)

print("Images resized successfully.")
