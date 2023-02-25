from PIL import Image
file = r'myImage/nature.jpg'
img = Image.open(file)
bw = img.convert('L')
print(list(bw.getdata()))
mono = img.convert('1')
rgba = img.convert('RGBA')
