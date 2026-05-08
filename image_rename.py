"""
quick script to rename photos in folder for ease of implementation into html file.
"""

import os

### folder containing trip specific subfolders
folder = '/Users/isaac_daviet/Desktop/coding/personal_website/assets/img/photos_page'

### trip subfolder names
trips = ['alps', 'florida', 'japan', 'new_york', 'north_cascades', 'oregon_coast', 'paris', 'southern_europe', 'sweden']

for trip in trips:
    subfolder = os.path.join(folder, trip)
    
    # Get only files (not directories), exclude hidden files
    files = [f for f in os.listdir(subfolder) 
             if os.path.isfile(os.path.join(subfolder, f)) and not f.startswith('.')]
    
    # Sort files for consistent ordering
    files.sort()
    
    # First rename to temporary names to avoid conflicts
    for i, f in enumerate(files):
        src = os.path.join(subfolder, f)
        tmp = os.path.join(subfolder, f'temp_{i}.png')
        os.rename(src, tmp)
    
    # Then rename to final names
    temp_files = sorted([f for f in os.listdir(subfolder) if f.startswith('temp_')])
    for i, f in enumerate(temp_files, 1):
        src = os.path.join(subfolder, f)
        dst = os.path.join(subfolder, f'photo_{i}.png')
        os.rename(src, dst)
    
    print(f"{trip}: renamed {len(files)} files")
