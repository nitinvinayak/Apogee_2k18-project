from PIL import Image,ImageOps

im=Image.open("q4.jpg")
im1=ImageOps.grayscale(im)
im1=ImageOps.autocontrast(im1,cutoff=50,ignore=0)
im1.save("q6.jpg")
