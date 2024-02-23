from PIL import Image
import os

def resize_images(input_folder, output_folder, new_size):
    for filename in os.listdir(input_folder):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            image_path = os.path.join(input_folder, filename)
            img = Image.open(image_path)

            # Resize the image
            img_resized = img.resize(new_size, Image.LANCZOS)

            # Save the resized image to the output folder
            output_path = os.path.join(output_folder, filename)
            img_resized.save(output_path)

# Set your input and output folders and desired size
input_folder = "C:\\Users\\MichaelDixon\\OneDrive - Dufrain Consulting\\Documents\\Python Scripts"
output_folder = "C:\\Users\\MichaelDixon\\OneDrive - Dufrain Consulting\\Documents\\Python Scripts\\Resized_Images"
new_size = (32, 32)  # Set the desired size in pixels

# Resize images
resize_images(input_folder, output_folder, new_size)