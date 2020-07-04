#copying and pasting Images onto Other Image

from PIL import Image
myimg = Image.open('me.JPG')
myimgcopy = catIm.copy()
faceIm = catIm.crop((335, 345, 565, 560))
print(faceIm.size)
myimgcopy.paste(faceIm, (0, 0))
myimgcopy.paste(faceIm, (400, 500))
myimgcopy.save('pasted.png')
