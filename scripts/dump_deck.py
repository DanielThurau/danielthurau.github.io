from pdf2image import convert_from_path
import os

def convert(pdf_path, output_folder, naming_scheme=""):
    images = convert_from_path(pdf_path)
    if not os.path.exists(output_folder):
        print(f"Error: Directory {output_folder} does not exist. Please create it")
        return 1

    for i, image in enumerate(images):
        filename = f"{output_folder}/{naming_scheme}_{i+1}.jpeg"
        image.save(filename, 'JPEG')
        print(f"Saved {filename}")


convert("desk.pdf", "example", "desk")
