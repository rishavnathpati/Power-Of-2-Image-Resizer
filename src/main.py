"""
Author: Rishav Nath Pati
This program resizes images to power of 2 for use in game engines.
"""

from __future__ import print_function
import sys
import os
import glob
from tkinter import Tk, Button, Label, Entry, filedialog, StringVar, IntVar, Toplevel, ttk
from PIL import Image
from PIL import TgaImagePlugin  # required import for cxfreeze to correctly package
from pygame import image
import threading

sizes = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]  # PO2 sizes

def get_closest(y):
    """Return the closest power of 2 greater than or equal to y."""
    return min((size for size in sizes if size >= y), default=sizes[-1])

def get_next_higher_po2(y):
    """Return the next higher power of 2 if exists, else return the highest power of 2 in sizes."""
    for size in sizes:
        if size > y:
            return size
    return sizes[-1]

def po2(im, threshold=0.25):
    """ 
    Return a resized image that is a power of 2 
    (Checking that if image size is reduced it was fairly close to that size anyway based on threshold)
    """
    width, height = im.size

    new_width = get_closest(width)
    new_height = get_closest(height)

    # Check if the new dimensions are smaller and within the threshold
    if new_width < width and (width - new_width) > int(new_width * threshold):
        new_width = get_next_higher_po2(new_width)
    
    if new_height < height and (height - new_height) > int(new_height * threshold):
        new_height = get_next_higher_po2(new_height)

    return im.resize((new_width, new_height), resample=Image.BICUBIC)

def po2_add(im):
    """Return an image resized to the nearest power of 2 by adding pixels (without distortion)."""
    width, height = im.size

    new_width = get_closest(width)
    new_height = get_closest(height)

    # Calculate the aspect ratio preserving size
    aspect_ratio = width / height
    if aspect_ratio > 1:  # Width is greater than height
        resize_width = new_width
        resize_height = int(new_width / aspect_ratio)
    else:  # Height is greater than width
        resize_height = new_height
        resize_width = int(new_height * aspect_ratio)
    
    resized_im = im.resize((resize_width, resize_height), resample=Image.BICUBIC)
    
    new_im = Image.new(im.mode, (new_width, new_height))

    # Calculate position to center the image
    left = (new_width - resize_width) // 2
    top = (new_height - resize_height) // 2

    new_im.paste(resized_im, (left, top))

    return new_im

def read_config():
    """Returns the threshold and compression level from the config file."""
    threshold = 0.25
    compression = 0

    try:
        with open('config.txt', 'r') as config:
            for line in config:
                if "THRESHOLD=" in line.upper():
                    try:
                        threshold = float(line.upper().replace('THRESHOLD=', ''))
                    except ValueError:
                        print('Invalid threshold in config.txt')
                
                if "COMPRESSION=" in line.upper():
                    try:
                        compression = int(line.upper().replace('COMPRESSION=', ''))
                    except ValueError:
                        print('Invalid compression level in config.txt')
    except IOError:
        print("Cannot open config.txt")

    return threshold, compression

def save_targa(im, arg):
    """Convert PIL image to pygame image and save. PIL cannot save tga and no other library works with PIL."""
    image.save(image.fromstring(im.tobytes(), im.size, im.mode), arg.split('.', 1)[0] + '.tga')

def process_image(file_path, threshold, compression):
    try:
        im = Image.open(file_path)
        if im.format.upper() == "TGA":
            save_targa(po2(im, threshold), file_path)
        else:
            resized_im = po2_add(im) if im.format.lower() == 'png' else po2(im, threshold)
            resized_im.save(file_path, im.format.lower(), compress_level=compression)
    except IOError:
        print("IO ERROR: Is file an image? -> ", file_path)

def process_path(input_path, threshold, compression):
    if os.path.isdir(input_path):
        # Batch process all images in the directory
        files = glob.glob(os.path.join(input_path, "*"))
    else:
        # Process a single image file
        files = [input_path]
    
    total_files = len(files)
    for i, file_path in enumerate(files):
        process_image(file_path, threshold, compression)
        progress = int((i + 1) / total_files * 100)
        update_progress(progress_var, progress)
    
    status_label.set("Processing complete")

def update_progress(progress_var, value):
    progress_var.set(value)

def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.tga;*.bmp;*.gif")])
    file_path.set(filename)

def browse_directory():
    directory = filedialog.askdirectory()
    file_path.set(directory)

def start_processing():
    input_path = file_path.get()
    threshold, compression = read_config()
    status_label.set("Processing...")
    progress_var.set(0)
    threading.Thread(target=process_path, args=(input_path, threshold, compression)).start()

def show_config_window():
    config_window = Toplevel(root)
    config_window.title("Settings")

    Label(config_window, text="Threshold:").grid(row=0, column=0, padx=10, pady=5)
    threshold_entry = Entry(config_window)
    threshold_entry.grid(row=0, column=1, padx=10, pady=5)

    Label(config_window, text="Compression Level:").grid(row=1, column=0, padx=10, pady=5)
    compression_entry = Entry(config_window)
    compression_entry.grid(row=1, column=1, padx=10, pady=5)

    def save_settings():
        with open('config.txt', 'w') as config_file:
            config_file.write(f"THRESHOLD={threshold_entry.get()}\n")
            config_file.write(f"COMPRESSION={compression_entry.get()}\n")
        config_window.destroy()

    Button(config_window, text="Save", command=save_settings).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

if __name__ == "__main__":
    root = Tk()
    root.title("Power Of 2 Image Resizer")

    file_path = StringVar()
    status_label = StringVar()
    progress_var = IntVar()

    Label(root, text="Select a file or directory:").grid(row=0, column=0, padx=10, pady=5)
    Entry(root, textvariable=file_path, width=50).grid(row=1, column=0, padx=10, pady=5)
    Button(root, text="Browse File", command=browse_file).grid(row=1, column=1, padx=5, pady=5)
    Button(root, text="Browse Directory", command=browse_directory).grid(row=1, column=2, padx=5, pady=5)
    Button(root, text="Start Processing", command=start_processing).grid(row=2, column=0, columnspan=3, padx=10, pady=10)
    Label(root, textvariable=status_label).grid(row=3, column=0, columnspan=3, padx=10, pady=5)
    ttk.Progressbar(root, variable=progress_var, maximum=100).grid(row=4, column=0, columnspan=3, padx=10, pady=10)
    Button(root, text="Settings", command=show_config_window).grid(row=5, column=0, columnspan=3, padx=10, pady=10)

    root.mainloop()
