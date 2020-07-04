#rotating Images

from PIL import Image
myimg = Image.open('me.JPG')
#rotating 90
myimg.rotate(90).save('rotated90.png')

#rotating 180
#myimg.rotate(180).save('rotated180.png')

#rotating 270
#myimg.rotate(270).save('rotated270.png')
