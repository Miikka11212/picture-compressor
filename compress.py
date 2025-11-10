import os
from PIL import Image

input_folder = "images"          #Folder for original size images
output_folder = "compressed"     # Folder to save compressed images
resize_ratio = 0.9               # e.g. 0.5 = half the width & height
jpeg_quality = 80                # 1-100, higher = better quality & larger size
compress_by_resolution = True    # True = resize, False = only reduce quality

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        if compress_by_resolution:
            # Resize by ratio
            new_width = int(img.width * resize_ratio)
            new_height = int(img.height * resize_ratio)
            img = img.resize((new_width, new_height), Image.LANCZOS)

        # Define output path
        output_path = os.path.join(output_folder, filename)

        # Save with reduced quality
        if filename.lower().endswith((".jpg", ".jpeg")):
            img.save(output_path, "JPEG", quality=jpeg_quality, optimize=True)
        else:
            img.save(output_path, "PNG", optimize=True)

        print(f"Compressed: {filename}")

print("\nDone! Compressed images saved to:", output_folder)
