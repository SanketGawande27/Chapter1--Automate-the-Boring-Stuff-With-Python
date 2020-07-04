#cropping images

from PIL import Image
myimgs = Image.open('me.JPG')
myimgs = catIm.crop((335, 345, 565, 560))
myimgs.save('cropped.png')
