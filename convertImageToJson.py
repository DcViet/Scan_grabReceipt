import os
import pytesseract
import json
from PIL import Image

# Path to the folder containing the images
image_folder = '/home/grab_image/image1403'

# Path to the output directory
output_folder = '/home/output_grab'

# Path to the output JSON file
output_file = os.path.join(output_folder, 'output_1403.json')

# List to store the extracted text from all the images
text_list = []

# Loop through all the images in the folder
for filename in os.listdir(image_folder):
    # Check if the file is an image (ends with .jpg, .jpeg, .png, etc.)
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        # Load the image using PIL
        img = Image.open(os.path.join(image_folder, filename))
        
        # Use Tesseract to extract text from the image
        text = pytesseract.image_to_string(img)

        # Append the extracted text to the list
        text_list.append(text)

# Create a JSON object with the extracted text list
data = {'text_list': text_list}

# Save the JSON object to a file
with open(output_file, 'w') as outfile:
    json.dump(data, outfile)
