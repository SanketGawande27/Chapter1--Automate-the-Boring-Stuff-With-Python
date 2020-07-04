#Adding logo 

import os
from PIL import Image
SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'tiger.png'

logoIm = Image.open('me.JPG')
logoWidth, logoHeight = logoIm.size
# Loop over all files in the working directory.
for filename in os.listdir('.'):
       if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == 'tiger.jpg':
           continue    # skip non-image files and the logo file itself

       im = Image.open(filename)
       width, height = im.size
       # Check if image needs to be resized.
       if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
         # Calculate the new width and height to resize to.
         if width > height:
               height = int((SQUARE_FIT_SIZE / width) * height)
               width = SQUARE_FIT_SIZE
         else:
               width = int((SQUARE_FIT_SIZE / height) * width)
               height = SQUARE_FIT_SIZE

           # Resize the image.
       print('Resizing %s...' % (filename))
       im = im.resize((width, height))
           # Add the logo.
          
       print('Adding logo to %s...' % (filename))
       im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

     # Save changes.
       im.save(os.path.join('withLogo.jpg', filename))
